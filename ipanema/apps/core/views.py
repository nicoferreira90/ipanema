from django.http import Http404
from django.shortcuts import render

from .sample_modules import MODULES, TOTAL_PLANNED


def index(request):
    return render(request, "index.html")


def prototype(request, num):
    if num not in (1, 2, 3, 4):
        raise Http404("No such prototype")
    context = {
        "modules": MODULES,
        "available_modules": [m for m in MODULES if m["status"] == "available"],
        "coming_modules": [m for m in MODULES if m["status"] == "coming_soon"],
        "total_planned": TOTAL_PLANNED,
    }
    return render(request, f"prototypes/proto_{num}.html", context)
