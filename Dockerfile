FROM python:3.8-slim-buster

ENV PYTHONUNBUFFERED=1

RUN apt-get update && apt-get install -y libpq-dev gcc

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt