"""Tests for the content system check (ipanema.apps.modules.checks)."""
from unittest.mock import patch

from django.test import SimpleTestCase

from ipanema.apps.modules import content
from ipanema.apps.modules.checks import check_content


def _module(status="available", lessons=None, project="default"):
    """Build a synthetic module dict shaped like content._load_module output."""
    if project == "default":
        project = {"title": "P", "check": "assert True"}
    return {
        "slug": "99-synthetic",
        "status": status,
        "lessons": lessons if lessons is not None else [],
        "project": project,
    }


def _lesson(key="99-synthetic/01-x", check="assert 1"):
    """Build a synthetic lesson dict."""
    return {"key": key, "check": check}


class CheckContentTests(SimpleTestCase):
    """Tests for check_content error detection."""

    def _ids(self, modules):
        """Run the check against a patched module list and return error ids."""
        with patch.object(content, "MODULES", modules):
            return {error.id for error in check_content(None)}

    def test_real_content_passes(self):
        """The real, shipped content produces no errors."""
        self.assertEqual(check_content(None), [])

    def test_available_module_without_lessons_raises_e001(self):
        """An available module with no lessons triggers modules.E001."""
        ids = self._ids([_module(lessons=[])])
        self.assertIn("modules.E001", ids)

    def test_lesson_with_empty_check_raises_e002(self):
        """A lesson with an empty check block triggers modules.E002."""
        ids = self._ids([_module(lessons=[_lesson(check="")])])
        self.assertIn("modules.E002", ids)

    def test_module_without_project_check_raises_e003(self):
        """An available module missing its project check triggers modules.E003."""
        ids = self._ids([_module(lessons=[_lesson()], project=None)])
        self.assertIn("modules.E003", ids)

    def test_coming_soon_modules_are_ignored(self):
        """A non-available module is skipped even if it's incomplete."""
        ids = self._ids([_module(status="coming_soon", lessons=[], project=None)])
        self.assertEqual(ids, set())
