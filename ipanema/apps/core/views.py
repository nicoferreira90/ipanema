from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .sample_modules import MODULES, TOTAL_PLANNED


@login_required
def progress(request):
    return render(request, "progress.html")


def index(request):
    context = {
        "modules": MODULES,
        "available_modules": [m for m in MODULES if m["status"] == "available"],
        "coming_modules": [m for m in MODULES if m["status"] == "coming_soon"],
        "total_planned": TOTAL_PLANNED,
    }
    return render(request, "index.html", context)
