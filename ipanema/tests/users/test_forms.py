"""Unit tests for the custom user forms."""
from django.contrib.auth import get_user_model
from django.test import TestCase

from ipanema.apps.users.forms import CustomUserChangeForm, CustomUserCreationForm

User = get_user_model()


class CustomUserCreationFormTests(TestCase):
    """Tests for CustomUserCreationForm."""

    def test_valid_form_creates_user(self):
        """A valid form saves a new user keyed by email."""
        form = CustomUserCreationForm(
            data={
                "email": "newuser@example.com",
                "password1": "s3cure-pass-123",
                "password2": "s3cure-pass-123",
            }
        )
        self.assertTrue(form.is_valid(), form.errors)
        user = form.save()
        self.assertEqual(user.email, "newuser@example.com")
        self.assertTrue(user.check_password("s3cure-pass-123"))

    def test_mismatched_passwords_invalid(self):
        """The form is invalid when the two passwords differ."""
        form = CustomUserCreationForm(
            data={
                "email": "newuser@example.com",
                "password1": "s3cure-pass-123",
                "password2": "different-pass-456",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)

    def test_duplicate_email_invalid(self):
        """The form is invalid when the email already exists."""
        User.objects.create_user(email="taken@example.com", password="pass1234")
        form = CustomUserCreationForm(
            data={
                "email": "taken@example.com",
                "password1": "s3cure-pass-123",
                "password2": "s3cure-pass-123",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)


class CustomUserChangeFormTests(TestCase):
    """Tests for CustomUserChangeForm."""

    def test_form_exposes_expected_fields(self):
        """The change form exposes email, first_name and last_name."""
        form = CustomUserChangeForm()
        self.assertEqual(
            set(form.fields) & {"email", "first_name", "last_name"},
            {"email", "first_name", "last_name"},
        )

    def test_blank_names_are_allowed(self):
        """first_name and last_name may be left blank."""
        user = User.objects.create_user(email="edit@example.com", password="pass1234")
        form = CustomUserChangeForm(
            data={"email": "edit@example.com", "first_name": "", "last_name": ""},
            instance=user,
        )
        self.assertTrue(form.is_valid(), form.errors)
