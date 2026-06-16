"""Unit tests for the modules progress models."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase

from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion

User = get_user_model()


class LessonCompletionTests(TestCase):
    """Tests for the LessonCompletion model."""

    def setUp(self):
        """Create a user to attach completions to."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )

    def test_create_sets_completed_at(self):
        """Creating a completion auto-populates completed_at."""
        row = LessonCompletion.objects.create(
            user=self.user, lesson_key="01-mod/01-lesson"
        )
        self.assertIsNotNone(row.completed_at)

    def test_str_format(self):
        """__str__ renders '<user> · <lesson_key>'."""
        row = LessonCompletion.objects.create(
            user=self.user, lesson_key="01-mod/01-lesson"
        )
        self.assertEqual(str(row), "learner@example.com · 01-mod/01-lesson")

    def test_unique_constraint_blocks_duplicates(self):
        """The same user+lesson_key cannot be stored twice."""
        LessonCompletion.objects.create(user=self.user, lesson_key="01-mod/01-lesson")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                LessonCompletion.objects.create(
                    user=self.user, lesson_key="01-mod/01-lesson"
                )

    def test_get_or_create_is_idempotent(self):
        """get_or_create returns the existing row the second time."""
        first, created1 = LessonCompletion.objects.get_or_create(
            user=self.user, lesson_key="01-mod/01-lesson"
        )
        second, created2 = LessonCompletion.objects.get_or_create(
            user=self.user, lesson_key="01-mod/01-lesson"
        )
        self.assertTrue(created1)
        self.assertFalse(created2)
        self.assertEqual(first.pk, second.pk)
        self.assertEqual(LessonCompletion.objects.count(), 1)

    def test_cascade_delete_with_user(self):
        """Deleting the user removes their lesson completions."""
        LessonCompletion.objects.create(user=self.user, lesson_key="01-mod/01-lesson")
        self.user.delete()
        self.assertEqual(LessonCompletion.objects.count(), 0)


class ModuleCompletionTests(TestCase):
    """Tests for the ModuleCompletion model."""

    def setUp(self):
        """Create a user to attach completions to."""
        self.user = User.objects.create_user(
            email="learner@example.com", password="pass1234"
        )

    def test_create_with_submission(self):
        """A module completion stores the submitted code."""
        row = ModuleCompletion.objects.create(
            user=self.user, module_slug="01-mod", submission="print('hi')"
        )
        self.assertEqual(row.submission, "print('hi')")
        self.assertIsNotNone(row.completed_at)

    def test_str_format(self):
        """__str__ renders '<user> · <module_slug>'."""
        row = ModuleCompletion.objects.create(user=self.user, module_slug="01-mod")
        self.assertEqual(str(row), "learner@example.com · 01-mod")

    def test_unique_constraint_blocks_duplicates(self):
        """The same user+module_slug cannot be stored twice."""
        ModuleCompletion.objects.create(user=self.user, module_slug="01-mod")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                ModuleCompletion.objects.create(user=self.user, module_slug="01-mod")

    def test_update_or_create_updates_submission(self):
        """update_or_create replaces the submission without duplicating rows."""
        ModuleCompletion.objects.update_or_create(
            user=self.user, module_slug="01-mod", defaults={"submission": "v1"}
        )
        row, created = ModuleCompletion.objects.update_or_create(
            user=self.user, module_slug="01-mod", defaults={"submission": "v2"}
        )
        self.assertFalse(created)
        self.assertEqual(row.submission, "v2")
        self.assertEqual(ModuleCompletion.objects.count(), 1)

    def test_cascade_delete_with_user(self):
        """Deleting the user removes their module completions."""
        ModuleCompletion.objects.create(user=self.user, module_slug="01-mod")
        self.user.delete()
        self.assertEqual(ModuleCompletion.objects.count(), 0)
