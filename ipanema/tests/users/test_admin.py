"""Tests for the CustomUser admin configuration and pages."""
from django.contrib.admin.sites import site
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

User = get_user_model()


class CustomUserAdminConfigTests(TestCase):
    """Tests for the registered CustomUserAdmin options."""

    def setUp(self):
        """Grab the registered admin instance for CustomUser."""
        self.admin = site._registry[User]

    def test_list_display(self):
        """The changelist shows the expected columns."""
        self.assertEqual(
            self.admin.list_display,
            ["email", "first_name", "last_name", "is_staff", "is_active"],
        )

    def test_list_filter(self):
        """The changelist filters on staff/active/superuser flags."""
        self.assertEqual(
            self.admin.list_filter, ["is_staff", "is_active", "is_superuser"]
        )

    def test_search_fields(self):
        """Admin search covers email and names."""
        self.assertEqual(
            self.admin.search_fields, ["email", "first_name", "last_name"]
        )

    def test_ordering(self):
        """Users are ordered by email."""
        self.assertEqual(self.admin.ordering, ["email"])

    def test_add_fieldsets_use_password_pair(self):
        """The add form collects password1/password2 (creation form)."""
        fields = self.admin.add_fieldsets[0][1]["fields"]
        self.assertIn("password1", fields)
        self.assertIn("password2", fields)


class CustomUserAdminPagesTests(TestCase):
    """Smoke tests that the admin pages render for a superuser."""

    def setUp(self):
        """Create and log in a superuser."""
        self.admin_user = User.objects.create_superuser(
            email="admin@example.com", password="pass1234"
        )
        self.client.force_login(self.admin_user)

    def test_changelist_renders(self):
        """The user changelist returns 200."""
        url = reverse("admin:users_customuser_changelist")
        self.assertEqual(self.client.get(url).status_code, 200)

    def test_add_page_renders(self):
        """The add-user page returns 200."""
        url = reverse("admin:users_customuser_add")
        self.assertEqual(self.client.get(url).status_code, 200)
