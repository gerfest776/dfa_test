FROM python:3.10-slim-buster

WORKDIR /app
COPY poetry.lock pyproject.toml /app/

RUN apt-get update && apt install -y netcat && pip install --upgrade pip poetry \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev \
    && rm -rf /root/.cache/pip
 \

COPY . /app
WORKDIR /app

RUN chmod +x ./entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]