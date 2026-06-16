"""Integration tests for the core landing and progress views."""
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from ipanema.apps.modules import content
from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion

User = get_user_model()

_AVAILABLE = content.AVAILABLE_MODULES[0]
MODULE_SLUG = _AVAILABLE["slug"]
FIRST_LESSON = _AVAILABLE["lessons"][0]["slug"]


class IndexViewTests(TestCase):
    """Tests for core:index (the landing page)."""

    def test_index_renders_for_anonymous(self):
        """The landing page returns 200 without auth and uses index.html."""
        response = self.client.get(reverse("core:index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "index.html")

    def test_index_context_keys(self):
        """The landing context exposes the keys the template relies on."""
        response = self.client.get(reverse("core:index"))
        for key in (
            "modules",
            "available_modules",
            "coming_modules",
            "first_module",
            "total_planned",
            "home_url",
        ):
            self.assertIn(key, response.context)


class ProgressViewTests(TestCase):
    """Tests for core:progress."""

    def setUp(self):
        """Create a learner and resolve the progress URL."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )
        self.url = reverse("core:progress")

    def test_anonymous_redirected_to_login(self):
        """An anonymous request is redirected to the login page."""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 302)
        self.assertIn("login", response.url)

    def test_authenticated_without_progress(self):
        """A learner with no completions sees an empty progress summary."""
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "progress.html")
        self.assertFalse(response.context["has_progress"])
        self.assertEqual(response.context["summary"], [])

    def test_summary_reflects_lesson_progress(self):
        """A completed lesson appears in the summary with the right counts."""
        LessonCompletion.objects.create(
            user=self.user, lesson_key=f"{MODULE_SLUG}/{FIRST_LESSON}"
        )
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertTrue(response.context["has_progress"])
        self.assertEqual(response.context["lesson_count"], 1)
        self.assertEqual(response.context["module_count"], 0)

        entry = next(
            row
            for row in response.context["summary"]
            if row["module"]["slug"] == MODULE_SLUG
        )
        self.assertEqual(entry["done"], 1)
        self.assertEqual(entry["total"], len(_AVAILABLE["lessons"]))
        self.assertFalse(entry["complete"])

    def test_summary_marks_completed_module(self):
        """A module completion marks the summary entry complete."""
        ModuleCompletion.objects.create(user=self.user, module_slug=MODULE_SLUG)
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.context["module_count"], 1)
        entry = next(
            row
            for row in response.context["summary"]
            if row["module"]["slug"] == MODULE_SLUG
        )
        self.assertTrue(entry["complete"])
