ARG PYTHON_VERSION=3.13-slim

# --- stage 1: compile the Tailwind/DaisyUI bundle (Node stays out of runtime) ---
FROM node:22-slim AS css
WORKDIR /build
COPY package.json package-lock.json ./
RUN npm ci
COPY ipanema/assets ./ipanema/assets
COPY ipanema/templates ./ipanema/templates
RUN npx tailwindcss -i ./ipanema/assets/app.css -o ./ipanema/static/css/app.css --minify

# --- stage 2: the Django runtime image ---
FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# install psycopg dependencies.
RUN apt-get update && apt-get install -y \
    libpq-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

# bring in the compiled stylesheet from the css stage (built fresh, wins over any
# stale copy in the build context)
COPY --from=css /build/ipanema/static/css/app.css /code/ipanema/static/css/app.css

ENV SECRET_KEY="build-only-dummy-key-not-used-at-runtime"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "ipanema.wsgi"]
