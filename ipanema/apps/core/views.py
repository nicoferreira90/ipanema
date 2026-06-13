from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ipanema.apps.modules import content
from ipanema.apps.modules.models import LessonCompletion, ModuleCompletion


@login_required
def progress(request):
    done_lessons = set(
        LessonCompletion.objects.filter(user=request.user).values_list(
            "lesson_key", flat=True
        )
    )
    done_modules = set(
        ModuleCompletion.objects.filter(user=request.user).values_list(
            "module_slug", flat=True
        )
    )

    summary = []
    for module in content.AVAILABLE_MODULES:
        done = sum(1 for lsn in module["lessons"] if lsn["key"] in done_lessons)
        if done or module["slug"] in done_modules:
            summary.append(
                {
                    "module": module,
                    "done": done,
                    "total": len(module["lessons"]),
                    "complete": module["slug"] in done_modules,
                }
            )

    context = {
        "summary": summary,
        "lesson_count": len(done_lessons),
        "module_count": len(done_modules),
        "has_progress": bool(summary),
    }
    return render(request, "progress.html", context)


def index(request):
    context = {
        "modules": content.MODULES,
        "available_modules": content.AVAILABLE_MODULES,
        "coming_modules": content.COMING_MODULES,
        "first_module": content.AVAILABLE_MODULES[0] if content.AVAILABLE_MODULES else None,
        "total_planned": content.TOTAL_PLANNED,
    }
    return render(request, "index.html", context)
