from django.conf import settings
from django.db import models


class LessonCompletion(models.Model):
    """A user finished one lesson's exercise. Row existence IS the fact.

    ``lesson_key`` is the content slug ``"<module-slug>/<lesson-slug>"`` — there
    is no FK to content (content lives in markdown files, not the DB).
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="lesson_completions",
    )
    lesson_key = models.CharField(max_length=80)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "lesson_key"], name="uniq_user_lesson"
            )
        ]
        ordering = ["completed_at"]

    def __str__(self):
        return f"{self.user} · {self.lesson_key}"


class ModuleCompletion(models.Model):
    """A user passed a module's mini-project — which marks the module complete.

    Stores the submitted code for later review. Keyed by the module content slug.
    """

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="module_completions",
    )
    module_slug = models.CharField(max_length=80)
    submission = models.TextField(blank=True)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "module_slug"], name="uniq_user_module"
            )
        ]
        ordering = ["completed_at"]

    def __str__(self):
        return f"{self.user} · {self.module_slug}"
