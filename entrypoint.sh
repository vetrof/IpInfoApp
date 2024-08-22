#!/bin/sh

# Установка gunicorn (если нужно устанавливать пакеты)
pip install gunicorn

# Выполнение миграций
python manage.py migrate

# Запуск приложения (выберите только один из вариантов)
# python manage.py runserver 0.0.0.0:8000  # Development server (не рекомендуется для production)
# gunicorn project.wsgi:application --bind 0.0.0.0:8000 --workers=$GUNICORN_WORKERS --threads=$GUNICORN_THREADS --reload  # Gunicorn для WSGI
daphne __settings.asgi:application -b 0.0.0.0 -p 8000  # Daphne для ASGI (поддержка WebSockets)

# Завершаем скрипт вызовом exec
exec "$@"
