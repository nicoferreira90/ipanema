"""Tests for the modules completion admin configuration."""
from django.contrib.admin.sites import site
from django.test import TestCase

from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion


class LessonCompletionAdminTests(TestCase):
    """Tests for LessonCompletionAdmin options."""

    def setUp(self):
        """Grab the registered admin instance."""
        self.admin = site._registry[LessonCompletion]

    def test_list_display(self):
        """The changelist shows user, lesson_key and completed_at."""
        self.assertEqual(
            self.admin.list_display, ["user", "lesson_key", "completed_at"]
        )

    def test_search_fields(self):
        """Search covers the user's email and the lesson_key."""
        self.assertEqual(self.admin.search_fields, ["user__email", "lesson_key"])

    def test_completed_at_readonly(self):
        """completed_at is read-only in the admin."""
        self.assertEqual(self.admin.readonly_fields, ["completed_at"])


class ModuleCompletionAdminTests(TestCase):
    """Tests for ModuleCompletionAdmin options."""

    def setUp(self):
        """Grab the registered admin instance."""
        self.admin = site._registry[ModuleCompletion]

    def test_list_display(self):
        """The changelist shows user, module_slug and completed_at."""
        self.assertEqual(
            self.admin.list_display, ["user", "module_slug", "completed_at"]
        )

    def test_search_fields(self):
        """Search covers the user's email and the module_slug."""
        self.assertEqual(self.admin.search_fields, ["user__email", "module_slug"])

    def test_completed_at_readonly(self):
        """completed_at is read-only in the admin."""
        self.assertEqual(self.admin.readonly_fields, ["completed_at"])
