# Ipanema

An interactive companion to Luciano Ramalho's *Fluent Python*. Read short
lessons, solve each exercise in a real Python terminal that runs in your browser,
and collect a stamp for every module you finish by passing its mini-project. The
whole thing wears a sunlit, postcard-and-philately theme.

## How it works

- **Lessons and exercises** are plain Markdown files, not database rows. They live
  under `ipanema/apps/modules/content/` and are parsed at server start.
- **The terminal** runs the learner's code entirely in the browser with
  [Pyodide](https://pyodide.org/) (CPython on WebAssembly). Nothing is executed on
  the server.
- **Progress** is recorded in Postgres when the exercise or mini-project checks
  pass. A finished mini-project marks the module complete and stores the
  submission (`LessonCompletion` / `ModuleCompletion`, keyed by content slug).

## Tech stack

- Django 6 with a custom, email-only user model
- PostgreSQL (via `psycopg` 3)
- django-allauth for authentication
- Tailwind CSS 4 and DaisyUI for styling
- Pyodide for the in-browser Python sandbox
- Gunicorn, Docker, and Fly.io for deployment

## Quick start

Prerequisites: Python 3.13, Node 22, and a running PostgreSQL.

    # 1. Python environment
    python -m venv .venv
    ./.venv/Scripts/activate        # Windows;  source .venv/bin/activate on macOS/Linux
    pip install -r requirements.txt

    # 2. Environment file
    cp ipanema/.env.example ipanema/.env    # then edit SECRET_KEY and DB settings

    # 3. Frontend CSS
    npm install
    npm run build:css               # or: npm run watch:css  (rebuild on change)

    # 4. Database and admin user
    python manage.py migrate
    python manage.py createsuperuser

    # 5. Run
    python manage.py runserver 8001

Then open http://127.0.0.1:8001/. The local Postgres is expected on port `6543`
(see `ipanema/.env.example`).

## Project layout

    ipanema/
      apps/
        core/        landing page and progress dashboard
        users/       custom email-only user model
        modules/     lessons, exercises, mini-projects, completion tracking
          content/   the Markdown course content (source of truth)
      templates/     Django templates (postcard theme, partials, account pages)
      assets/        Tailwind CSS source (app.css)
      static/        compiled CSS and JS (runner.js drives the Pyodide terminal)
      settings.py
    manage.py
    Dockerfile       two-stage build: compile CSS, then the Django runtime

## Deployment

The `Dockerfile` builds the Tailwind bundle in a Node stage, then bakes a Gunicorn
image that serves `ipanema.wsgi`. It is set up for [Fly.io](https://fly.io/);
provide `SECRET_KEY`, `DEBUG=False`, and the `POSTGRES_*` variables as secrets.
