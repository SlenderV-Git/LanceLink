FROM python:3.9.5-slim-buster

ARG app_root=/app
WORKDIR /app

COPY ./poetry.lock ./pyproject.toml ${app_root}/
COPY ./hello-nginx-app ${app_root}/

RUN pip install poetry==1.1.3
RUN poetry install && poetry cache clear --all -n pypi
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0"]
