#!/bin/sh

python manage.py migrate
#python manage.py runserver 0.0.0.0:8000  # Development server (не рекомендуется для production)
gunicorn __settings.wsgi:application --bind 0.0.0.0:8000 --workers=$GUNICORN_WORKERS --threads=$GUNICORN_THREADS --reload
#daphne __settings.asgi:application -b 0.0.0.0 -p 8000  # Daphne для ASGI (поддержка WebSockets)

exec "$@"
