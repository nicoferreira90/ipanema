"""Load module/lesson content from markdown files into memory.

The markdown files under ``content/`` are the source of truth for all course
content (modules, lessons, exercises, mini-projects). They are parsed once at
import time into plain dicts that mirror the shape the templates consume, so
the landing page's "Collection" section keeps working unchanged.

Layout::

    content/NN-slug/_module.md          module metadata + mini-project
    content/NN-slug/NN-lesson-slug.md    one lesson

Each file is YAML frontmatter + a markdown body. Directory/file ``NN-`` prefixes
give both ordering and the stable slug that progress rows key on. Those slugs
are an append-only contract once any user has progress — don't rename them.
"""
from pathlib import Path

import frontmatter
import markdown as _markdown

CONTENT_DIR = Path(__file__).resolve().parent / "content"
TOTAL_PLANNED = 30

_MD_EXTENSIONS = ["fenced_code", "tables"]


def _render(text):
    """Render a markdown string to HTML (empty string for falsy input)."""
    return _markdown.markdown(text or "", extensions=_MD_EXTENSIONS)


def _number_from(name):
    """Pull the leading ``NN`` integer off a ``NN-slug`` directory/file name."""
    head = name.split("-", 1)[0]
    return int(head) if head.isdigit() else 0


def _load_lesson(path, module_slug):
    """Parse a single lesson file into a dict."""
    post = frontmatter.load(str(path))
    meta = post.metadata
    slug = path.stem  # e.g. "04-string-representation"
    return {
        "number": _number_from(slug),
        "slug": slug,
        "key": f"{module_slug}/{slug}",
        "title": meta.get("title", slug),
        "body_html": _render(post.content),
        "exercise": (meta.get("exercise") or "").strip(),
        "check": (meta.get("check") or "").strip(),
    }


def _load_module(directory):
    """Parse a module directory (``_module.md`` + lesson files) into a dict."""
    post = frontmatter.load(str(directory / "_module.md"))
    meta = post.metadata
    slug = directory.name  # e.g. "01-the-python-data-model"

    lessons = [
        _load_lesson(p, slug)
        for p in sorted(directory.glob("*.md"))
        if p.name != "_module.md"
    ]
    lessons.sort(key=lambda lsn: lsn["number"])

    project = meta.get("project")
    if project:
        project = {
            "title": project.get("title", ""),
            "brief": (project.get("brief") or "").strip(),
            "brief_html": _render(project.get("brief")),
            "check": (project.get("check") or "").strip(),
        }

    intro = post.content.strip()
    return {
        "number": _number_from(slug),
        "slug": slug,
        "title": meta.get("title", slug),
        "part": meta.get("part", ""),
        "tagline": meta.get("tagline", ""),
        "color": meta.get("color", "coral"),
        "status": meta.get("status", "coming_soon"),
        "blurb": intro,
        "intro_html": _render(post.content),
        "lessons": lessons,
        "exercise_count": len(lessons),
        "project": project,
    }


def _load_all():
    modules = [
        _load_module(d)
        for d in sorted(CONTENT_DIR.iterdir())
        if d.is_dir() and (d / "_module.md").exists()
    ]
    modules.sort(key=lambda m: m["number"])
    return modules


# Parsed once at import; the files are the source of truth, not a cache.
MODULES = _load_all()
_BY_SLUG = {m["slug"]: m for m in MODULES}
AVAILABLE_MODULES = [m for m in MODULES if m["status"] == "available"]
COMING_MODULES = [m for m in MODULES if m["status"] != "available"]


def get_module(slug):
    """Return the module dict for ``slug`` or ``None``."""
    return _BY_SLUG.get(slug)


def get_lesson(module_slug, lesson_slug):
    """Return ``(module, lesson)`` for the given slugs, or ``(module, None)`` /
    ``(None, None)`` when missing."""
    module = _BY_SLUG.get(module_slug)
    if module is None:
        return None, None
    for lesson in module["lessons"]:
        if lesson["slug"] == lesson_slug:
            return module, lesson
    return module, None
