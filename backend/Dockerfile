# Базовый образ с Python 3.11.5
FROM python:3.11.5-slim

# Установка зависимостей системы
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Установка Poetry
RUN curl -sSL https://install.python-poetry.org | python3 -

# Создание и установка рабочей директории
WORKDIR /app

# Копирование файлов проекта
COPY pyproject.toml poetry.lock ./

# Установка зависимостей проекта
RUN /root/.local/bin/poetry config virtualenvs.create false \
    && /root/.local/bin/poetry install --no-interaction --no-ansi

# Копирование остальных файлов проекта
COPY . .

# Открытие порта для приложения
EXPOSE 8000
