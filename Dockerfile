FROM python:3.10

# Настройки среды
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Установка рабочей директории
WORKDIR /code

# Копируем и устанавливаем зависимости
COPY ./requirements.txt .
RUN pip install -r requirements.txt gunicorn

# Установка Nginx
RUN apt-get update && apt-get install -y nginx && rm -rf /var/lib/apt/lists/*

# Копируем весь проект
COPY . .

# Копируем конфиг для Nginx
COPY ./nginx.conf /etc/nginx/nginx.conf

# Копируем и даем права на выполнение скрипта
COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Определяем точку входа
ENTRYPOINT ["/entrypoint.sh"]
