# syntax=docker/dockerfile:1
FROM python:3.12.4-slim-bookworm AS builder

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./app ./app