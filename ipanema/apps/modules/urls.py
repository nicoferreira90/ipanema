from django.urls import path

from . import views

app_name = "modules"

urlpatterns = [
    path("<slug:module_slug>/", views.module_detail, name="module_detail"),
    path(
        "<slug:module_slug>/complete/",
        views.complete_module,
        name="complete_module",
    ),
    path(
        "<slug:module_slug>/<slug:lesson_slug>/",
        views.lesson_detail,
        name="lesson_detail",
    ),
    path(
        "<slug:module_slug>/<slug:lesson_slug>/complete/",
        views.complete_lesson,
        name="complete_lesson",
    ),
]
