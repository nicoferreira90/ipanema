"""System checks that validate authored content at boot / ``manage.py check``."""
from django.core.checks import Error, register

from . import content


@register()
def check_content(app_configs, **kwargs):
    errors = []
    for module in content.MODULES:
        if module["status"] != "available":
            continue
        if not module["lessons"]:
            errors.append(
                Error(
                    f"Available module '{module['slug']}' has no lessons.",
                    id="modules.E001",
                )
            )
        for lesson in module["lessons"]:
            if not lesson["check"]:
                errors.append(
                    Error(
                        f"Lesson '{lesson['key']}' has an empty check block.",
                        id="modules.E002",
                    )
                )
        project = module["project"]
        if not project or not project["check"]:
            errors.append(
                Error(
                    f"Available module '{module['slug']}' is missing a "
                    f"mini-project check block.",
                    id="modules.E003",
                )
            )
    return errors
