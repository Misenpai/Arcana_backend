FROM python:3.11-slim
WORKDIR /app
RUN apt-get update && apt-get install -y --no-install-recommends build-essential && apt-get clean && rm -rf /var/lib/apt/lists/*
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN mkdir -p /app/db && chmod 777 /app/db
ENV DJANGO_SETTINGS_MODULE=arcana_backend.settings.production
RUN python manage.py collectstatic --noinput
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "arcana_backend.wsgi:application"]