"""Unit tests for the CustomUser model and its manager."""
from django.contrib.auth import get_user_model
from django.db import IntegrityError, transaction
from django.test import TestCase

User = get_user_model()


class CustomUserManagerTests(TestCase):
    """Tests for CustomUserManager.create_user / create_superuser."""

    def test_create_user_with_email(self):
        """A regular user is created with the given email and password."""
        user = User.objects.create_user(email="test@example.com", password="pass1234")
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("pass1234"))
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_normalizes_email_domain(self):
        """The email domain is normalized (lower-cased) on creation."""
        user = User.objects.create_user(email="Test@EXAMPLE.COM", password="pass1234")
        self.assertEqual(user.email, "Test@example.com")

    def test_create_user_without_email_raises_value_error(self):
        """Creating a user without an email raises ValueError."""
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="pass1234")

    def test_create_superuser_sets_staff_and_superuser(self):
        """A superuser is created with is_staff and is_superuser True."""
        admin = User.objects.create_superuser(
            email="admin@example.com", password="pass1234"
        )
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)
        self.assertTrue(admin.is_active)

    def test_create_superuser_rejects_non_staff(self):
        """create_superuser rejects is_staff=False."""
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin@example.com", password="pass1234", is_staff=False
            )

    def test_create_superuser_rejects_non_superuser(self):
        """create_superuser rejects is_superuser=False."""
        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email="admin@example.com", password="pass1234", is_superuser=False
            )


class CustomUserModelTests(TestCase):
    """Tests for CustomUser fields and helper methods."""

    def test_str_returns_email(self):
        """__str__ returns the user's email."""
        user = User.objects.create_user(email="who@example.com", password="pass1234")
        self.assertEqual(str(user), "who@example.com")

    def test_get_full_name_with_names(self):
        """get_full_name joins first and last name."""
        user = User.objects.create_user(
            email="who@example.com",
            password="pass1234",
            first_name="Ada",
            last_name="Lovelace",
        )
        self.assertEqual(user.get_full_name(), "Ada Lovelace")

    def test_get_full_name_falls_back_to_email(self):
        """get_full_name returns the email when no names are set."""
        user = User.objects.create_user(email="who@example.com", password="pass1234")
        self.assertEqual(user.get_full_name(), "who@example.com")

    def test_get_short_name_prefers_first_name(self):
        """get_short_name returns first_name when set."""
        user = User.objects.create_user(
            email="who@example.com", password="pass1234", first_name="Ada"
        )
        self.assertEqual(user.get_short_name(), "Ada")

    def test_get_short_name_falls_back_to_email(self):
        """get_short_name returns the email when first_name is blank."""
        user = User.objects.create_user(email="who@example.com", password="pass1234")
        self.assertEqual(user.get_short_name(), "who@example.com")

    def test_email_must_be_unique(self):
        """A duplicate email raises IntegrityError."""
        User.objects.create_user(email="dupe@example.com", password="pass1234")
        with self.assertRaises(IntegrityError):
            with transaction.atomic():
                User.objects.create_user(email="dupe@example.com", password="pass5678")
