"""End-to-end integration tests spanning auth, modules and progress."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ipanema.apps.modules import content
from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion

User = get_user_model()

_AVAILABLE = content.AVAILABLE_MODULES[0]
MODULE_SLUG = _AVAILABLE["slug"]
LESSON_SLUGS = [lesson["slug"] for lesson in _AVAILABLE["lessons"]]


class LearnerJourneyTests(TestCase):
    """The full path: sign up, study a lesson, pass the mini-project, review."""

    def test_signup_then_complete_first_lesson_and_project(self):
        """A new learner signs up and makes progress that the dashboard reflects."""
        # Step 1: sign up via allauth (email verification is off -> auto-login).
        signup = self.client.post(
            reverse("account_signup"),
            {
                "email": "journey@example.com",
                "password1": "s3cure-pass-123",
                "password2": "s3cure-pass-123",
            },
        )
        self.assertEqual(signup.status_code, 302)
        user = User.objects.get(email="journey@example.com")

        # Step 2: the new session lands on the (login-required) progress page.
        progress = self.client.get(reverse("core:progress"))
        self.assertEqual(progress.status_code, 200)
        self.assertFalse(progress.context["has_progress"])

        # Step 3: open the module, then its first lesson.
        first_lesson = LESSON_SLUGS[0]
        self.assertEqual(
            self.client.get(
                reverse("modules:module_detail", args=[MODULE_SLUG])
            ).status_code,
            200,
        )
        self.assertEqual(
            self.client.get(
                reverse("modules:lesson_detail", args=[MODULE_SLUG, first_lesson])
            ).status_code,
            200,
        )

        # Step 4: complete the lesson exercise.
        self.client.post(
            reverse("modules:complete_lesson", args=[MODULE_SLUG, first_lesson])
        )
        self.assertTrue(
            LessonCompletion.objects.filter(
                user=user, lesson_key=f"{MODULE_SLUG}/{first_lesson}"
            ).exists()
        )

        # Step 5: pass the mini-project, which completes the module.
        self.client.post(
            reverse("modules:complete_module", args=[MODULE_SLUG]),
            {"code": "class Vector: ..."},
        )
        self.assertTrue(
            ModuleCompletion.objects.filter(
                user=user, module_slug=MODULE_SLUG
            ).exists()
        )

        # Step 6: the dashboard now reflects all of it.
        final = self.client.get(reverse("core:progress"))
        self.assertTrue(final.context["has_progress"])
        self.assertEqual(final.context["lesson_count"], 1)
        self.assertEqual(final.context["module_count"], 1)
        entry = next(
            row
            for row in final.context["summary"]
            if row["module"]["slug"] == MODULE_SLUG
        )
        self.assertEqual(entry["done"], 1)
        self.assertTrue(entry["complete"])

    def test_completing_every_lesson_and_project_marks_module_done(self):
        """Completing all lessons + the project flips module_done on the detail page."""
        user = User.objects.create_user(
            email="finisher@example.com", password="pass1234"
        )
        self.client.force_login(user)

        for lesson_slug in LESSON_SLUGS:
            self.client.post(
                reverse("modules:complete_lesson", args=[MODULE_SLUG, lesson_slug])
            )
        self.client.post(
            reverse("modules:complete_module", args=[MODULE_SLUG]), {"code": "done"}
        )

        detail = self.client.get(reverse("modules:module_detail", args=[MODULE_SLUG]))
        self.assertEqual(detail.context["done_count"], len(LESSON_SLUGS))
        self.assertTrue(detail.context["module_done"])

        progress = self.client.get(reverse("core:progress"))
        entry = next(
            row
            for row in progress.context["summary"]
            if row["module"]["slug"] == MODULE_SLUG
        )
        self.assertEqual(entry["done"], entry["total"])
        self.assertTrue(entry["complete"])
