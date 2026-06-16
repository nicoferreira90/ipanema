"""Tests for the markdown content loader (ipanema.apps.modules.content)."""
import tempfile
from pathlib import Path
from unittest.mock import patch

from django.test import SimpleTestCase

from ipanema.apps.modules import content

MODULE_SLUG = "01-the-python-data-model"


class HelperFunctionTests(SimpleTestCase):
    """Tests for the small pure helpers."""

    def test_number_from_extracts_prefix(self):
        """_number_from reads the leading NN integer off a name."""
        self.assertEqual(content._number_from("01-the-thing"), 1)
        self.assertEqual(content._number_from("12-another"), 12)

    def test_number_from_without_prefix_is_zero(self):
        """_number_from returns 0 when there's no numeric prefix."""
        self.assertEqual(content._number_from("no-prefix"), 0)

    def test_render_produces_html(self):
        """_render turns markdown into HTML."""
        self.assertIn("<h1>", content._render("# Hi"))

    def test_render_handles_fenced_code(self):
        """_render supports fenced code blocks."""
        html = content._render("```\nx = 1\n```")
        self.assertIn("<code>", html)

    def test_render_empty_returns_empty_string(self):
        """_render returns an empty string for falsy input."""
        self.assertEqual(content._render(""), "")
        self.assertEqual(content._render(None), "")


class ContentInvariantTests(SimpleTestCase):
    """Tests on the real, loaded content structures."""

    def test_modules_loaded(self):
        """At least one module is loaded."""
        self.assertGreater(len(content.MODULES), 0)

    def test_total_planned(self):
        """TOTAL_PLANNED is the documented 30."""
        self.assertEqual(content.TOTAL_PLANNED, 30)

    def test_available_and_coming_partition_modules(self):
        """AVAILABLE_MODULES and COMING_MODULES partition MODULES by status."""
        available = {m["slug"] for m in content.AVAILABLE_MODULES}
        coming = {m["slug"] for m in content.COMING_MODULES}
        everything = {m["slug"] for m in content.MODULES}
        self.assertEqual(available | coming, everything)
        self.assertEqual(available & coming, set())

    def test_available_modules_have_status_available(self):
        """Every available module actually has status 'available'."""
        for module in content.AVAILABLE_MODULES:
            self.assertEqual(module["status"], "available")

    def test_available_modules_are_complete(self):
        """Each available module has lessons and a project with a check."""
        for module in content.AVAILABLE_MODULES:
            self.assertTrue(module["lessons"], module["slug"])
            self.assertTrue(module["project"], module["slug"])
            self.assertTrue(module["project"]["check"], module["slug"])

    def test_lesson_keys_are_namespaced(self):
        """Each lesson key is '<module-slug>/<lesson-slug>'."""
        for module in content.MODULES:
            for lesson in module["lessons"]:
                self.assertEqual(
                    lesson["key"], f"{module['slug']}/{lesson['slug']}"
                )

    def test_get_module_known_and_unknown(self):
        """get_module returns a dict for a real slug and None otherwise."""
        self.assertIsNotNone(content.get_module(MODULE_SLUG))
        self.assertIsNone(content.get_module("does-not-exist"))

    def test_get_lesson_three_cases(self):
        """get_lesson handles found / missing-lesson / missing-module."""
        module = content.get_module(MODULE_SLUG)
        lesson_slug = module["lessons"][0]["slug"]

        found_module, found_lesson = content.get_lesson(MODULE_SLUG, lesson_slug)
        self.assertIsNotNone(found_module)
        self.assertIsNotNone(found_lesson)

        m2, no_lesson = content.get_lesson(MODULE_SLUG, "nope")
        self.assertIsNotNone(m2)
        self.assertIsNone(no_lesson)

        no_module, no_lesson2 = content.get_lesson("nope", "nope")
        self.assertIsNone(no_module)
        self.assertIsNone(no_lesson2)


class LoaderAgainstTempDirTests(SimpleTestCase):
    """Tests for _load_module / _load_all using a synthetic content dir."""

    def _write_module(self, root):
        """Write a minimal but valid module + two lessons under root."""
        module_dir = Path(root) / "09-temp-module"
        module_dir.mkdir()
        (module_dir / "_module.md").write_text(
            "---\n"
            "title: Temp Module\n"
            "part: Part Z\n"
            "tagline: just testing\n"
            "color: teal\n"
            "status: available\n"
            "project:\n"
            "  title: Temp Project\n"
            "  brief: Do the thing.\n"
            "  check: assert True\n"
            "---\n\n"
            "Intro text.\n",
            encoding="utf-8",
        )
        # Written out of order to prove the loader sorts by number.
        (module_dir / "02-second.md").write_text(
            "---\ntitle: Second\nexercise: do b\ncheck: assert 2\n---\n\nBody two.\n",
            encoding="utf-8",
        )
        (module_dir / "01-first.md").write_text(
            "---\ntitle: First\nexercise: do a\ncheck: assert 1\n---\n\nBody one.\n",
            encoding="utf-8",
        )
        return module_dir

    def test_load_module_parses_metadata_and_sorts_lessons(self):
        """_load_module parses frontmatter, the project, and orders lessons."""
        with tempfile.TemporaryDirectory() as root:
            module_dir = self._write_module(root)
            module = content._load_module(module_dir)

        self.assertEqual(module["slug"], "09-temp-module")
        self.assertEqual(module["number"], 9)
        self.assertEqual(module["title"], "Temp Module")
        self.assertEqual(module["status"], "available")
        self.assertEqual([l["number"] for l in module["lessons"]], [1, 2])
        self.assertEqual(module["lessons"][0]["key"], "09-temp-module/01-first")
        self.assertEqual(module["project"]["title"], "Temp Project")
        self.assertEqual(module["project"]["check"], "assert True")

    def test_load_all_discovers_modules_in_temp_dir(self):
        """_load_all picks up directories that contain a _module.md."""
        with tempfile.TemporaryDirectory() as root:
            self._write_module(root)
            with patch.object(content, "CONTENT_DIR", Path(root)):
                modules = content._load_all()
        self.assertEqual(len(modules), 1)
        self.assertEqual(modules[0]["slug"], "09-temp-module")
