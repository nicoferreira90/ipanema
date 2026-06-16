"""Integration tests for the modules views."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ipanema.apps.modules import content
from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion

User = get_user_model()

# Derive real slugs from the loaded content so the tests survive prose edits.
_AVAILABLE = content.AVAILABLE_MODULES[0]
MODULE_SLUG = _AVAILABLE["slug"]
LESSON_SLUGS = [lesson["slug"] for lesson in _AVAILABLE["lessons"]]
FIRST_LESSON = LESSON_SLUGS[0]
LAST_LESSON = LESSON_SLUGS[-1]
COMING_SLUG = content.COMING_MODULES[0]["slug"]


class ModuleDetailViewTests(TestCase):
    """Tests for modules:module_detail."""

    def setUp(self):
        """Create a learner."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )

    def test_valid_module_renders(self):
        """A real module slug returns 200 with the detail template."""
        url = reverse("modules:module_detail", args=[MODULE_SLUG])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modules/module_detail.html")

    def test_unknown_module_is_404(self):
        """A bogus module slug returns 404."""
        url = reverse("modules:module_detail", args=["no-such-module"])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_done_count_reflects_completions(self):
        """done_count and lesson.done reflect the user's progress."""
        LessonCompletion.objects.create(
            user=self.user, lesson_key=f"{MODULE_SLUG}/{FIRST_LESSON}"
        )
        self.client.force_login(self.user)
        response = self.client.get(reverse("modules:module_detail", args=[MODULE_SLUG]))
        self.assertEqual(response.context["done_count"], 1)
        done_flags = {
            lesson["slug"]: lesson["done"] for lesson in response.context["lessons"]
        }
        self.assertTrue(done_flags[FIRST_LESSON])

    def test_module_done_flag(self):
        """module_done is True once a ModuleCompletion exists."""
        ModuleCompletion.objects.create(user=self.user, module_slug=MODULE_SLUG)
        self.client.force_login(self.user)
        response = self.client.get(reverse("modules:module_detail", args=[MODULE_SLUG]))
        self.assertTrue(response.context["module_done"])


class LessonDetailViewTests(TestCase):
    """Tests for modules:lesson_detail."""

    def test_valid_lesson_renders(self):
        """A real lesson returns 200 with the lesson template."""
        url = reverse("modules:lesson_detail", args=[MODULE_SLUG, FIRST_LESSON])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modules/lesson_detail.html")

    def test_unknown_module_is_404(self):
        """A bogus module slug returns 404."""
        url = reverse("modules:lesson_detail", args=["nope", FIRST_LESSON])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_unknown_lesson_is_404(self):
        """A bogus lesson slug returns 404."""
        url = reverse("modules:lesson_detail", args=[MODULE_SLUG, "nope"])
        self.assertEqual(self.client.get(url).status_code, 404)

    def test_first_lesson_navigation(self):
        """The first lesson has no prev, position 1 and the right total."""
        url = reverse("modules:lesson_detail", args=[MODULE_SLUG, FIRST_LESSON])
        response = self.client.get(url)
        self.assertIsNone(response.context["prev"])
        self.assertEqual(response.context["position"], 1)
        self.assertEqual(response.context["total"], len(LESSON_SLUGS))

    def test_last_lesson_navigation(self):
        """The last lesson has no next and position equal to the total."""
        url = reverse("modules:lesson_detail", args=[MODULE_SLUG, LAST_LESSON])
        response = self.client.get(url)
        self.assertIsNone(response.context["next"])
        self.assertEqual(response.context["position"], len(LESSON_SLUGS))


class CompleteLessonViewTests(TestCase):
    """Tests for modules:complete_lesson."""

    def setUp(self):
        """Create a learner and resolve the completion URL."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )
        self.url = reverse(
            "modules:complete_lesson", args=[MODULE_SLUG, FIRST_LESSON]
        )

    def test_anonymous_post_redirects_to_login(self):
        """An anonymous POST is redirected to the login page."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_get_not_allowed(self):
        """GET is rejected (the view is POST-only)."""
        self.client.force_login(self.user)
        self.assertEqual(self.client.get(self.url).status_code, 405)

    def test_post_records_completion(self):
        """An authed POST records the completion and renders the partial."""
        self.client.force_login(self.user)
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modules/partials/lesson_done.html")
        self.assertTrue(
            LessonCompletion.objects.filter(
                user=self.user, lesson_key=f"{MODULE_SLUG}/{FIRST_LESSON}"
            ).exists()
        )

    def test_post_is_idempotent(self):
        """Posting twice records the completion only once."""
        self.client.force_login(self.user)
        self.client.post(self.url)
        self.client.post(self.url)
        self.assertEqual(LessonCompletion.objects.count(), 1)

    def test_unknown_lesson_is_404(self):
        """Completing a bogus lesson returns 404."""
        self.client.force_login(self.user)
        url = reverse("modules:complete_lesson", args=[MODULE_SLUG, "nope"])
        self.assertEqual(self.client.post(url).status_code, 404)


class CompleteModuleViewTests(TestCase):
    """Tests for modules:complete_module."""

    def setUp(self):
        """Create a learner and resolve the completion URL."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )
        self.url = reverse("modules:complete_module", args=[MODULE_SLUG])

    def test_anonymous_post_redirects_to_login(self):
        """An anonymous POST is redirected to the login page."""
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_post_records_submission(self):
        """An authed POST stores the submitted code and renders the partial."""
        self.client.force_login(self.user)
        response = self.client.post(self.url, {"code": "print('hi')"})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "modules/partials/module_done.html")
        row = ModuleCompletion.objects.get(user=self.user, module_slug=MODULE_SLUG)
        self.assertEqual(row.submission, "print('hi')")

    def test_post_updates_submission(self):
        """Re-posting updates the stored submission without duplicating rows."""
        self.client.force_login(self.user)
        self.client.post(self.url, {"code": "v1"})
        self.client.post(self.url, {"code": "v2"})
        self.assertEqual(ModuleCompletion.objects.count(), 1)
        row = ModuleCompletion.objects.get(user=self.user, module_slug=MODULE_SLUG)
        self.assertEqual(row.submission, "v2")

    def test_module_without_project_is_404(self):
        """Completing a module that has no mini-project returns 404."""
        self.client.force_login(self.user)
        url = reverse("modules:complete_module", args=[COMING_SLUG])
        self.assertEqual(self.client.post(url, {"code": "x"}).status_code, 404)
