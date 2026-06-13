from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render
from django.views.decorators.http import require_POST

from . import content
from .models import LessonCompletion, ModuleCompletion


def _done_keys(user):
    """Return (set of completed lesson_keys, set of completed module_slugs)."""
    if not user.is_authenticated:
        return set(), set()
    lessons = set(
        LessonCompletion.objects.filter(user=user).values_list("lesson_key", flat=True)
    )
    modules = set(
        ModuleCompletion.objects.filter(user=user).values_list(
            "module_slug", flat=True
        )
    )
    return lessons, modules


def module_detail(request, module_slug):
    module = content.get_module(module_slug)
    if module is None:
        raise Http404("No such module")

    done_lessons, done_modules = _done_keys(request.user)
    lessons = [
        {**lesson, "done": lesson["key"] in done_lessons}
        for lesson in module["lessons"]
    ]
    return render(
        request,
        "modules/module_detail.html",
        {
            "module": module,
            "lessons": lessons,
            "module_done": module_slug in done_modules,
            "done_count": sum(1 for lsn in lessons if lsn["done"]),
        },
    )


def lesson_detail(request, module_slug, lesson_slug):
    module, lesson = content.get_lesson(module_slug, lesson_slug)
    if module is None or lesson is None:
        raise Http404("No such lesson")

    done_lessons, _ = _done_keys(request.user)
    lessons = module["lessons"]
    idx = next(i for i, lsn in enumerate(lessons) if lsn["slug"] == lesson_slug)
    return render(
        request,
        "modules/lesson_detail.html",
        {
            "module": module,
            "lesson": lesson,
            "done": lesson["key"] in done_lessons,
            "prev": lessons[idx - 1] if idx > 0 else None,
            "next": lessons[idx + 1] if idx + 1 < len(lessons) else None,
            "position": idx + 1,
            "total": len(lessons),
        },
    )


@login_required
@require_POST
def complete_lesson(request, module_slug, lesson_slug):
    module, lesson = content.get_lesson(module_slug, lesson_slug)
    if module is None or lesson is None:
        raise Http404("No such lesson")

    LessonCompletion.objects.get_or_create(
        user=request.user, lesson_key=lesson["key"]
    )
    return render(request, "modules/partials/lesson_done.html", {"lesson": lesson})


@login_required
@require_POST
def complete_module(request, module_slug):
    module = content.get_module(module_slug)
    if module is None or not module["project"]:
        raise Http404("No such mini-project")

    ModuleCompletion.objects.update_or_create(
        user=request.user,
        module_slug=module_slug,
        defaults={"submission": request.POST.get("code", "")},
    )
    return render(request, "modules/partials/module_done.html", {"module": module})
