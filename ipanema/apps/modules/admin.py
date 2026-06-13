from django.contrib import admin

from .models import LessonCompletion, ModuleCompletion


@admin.register(LessonCompletion)
class LessonCompletionAdmin(admin.ModelAdmin):
    list_display = ["user", "lesson_key", "completed_at"]
    list_filter = ["completed_at"]
    search_fields = ["user__email", "lesson_key"]
    readonly_fields = ["completed_at"]


@admin.register(ModuleCompletion)
class ModuleCompletionAdmin(admin.ModelAdmin):
    list_display = ["user", "module_slug", "completed_at"]
    list_filter = ["completed_at"]
    search_fields = ["user__email", "module_slug"]
    readonly_fields = ["completed_at"]
