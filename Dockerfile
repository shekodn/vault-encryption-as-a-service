FROM python:3.7.7

ARG APP=api

ENV PYTHONUNBUFFERED 1

RUN mkdir /${APP}

WORKDIR /${APP}

COPY requirements.txt /${APP}/

RUN pip install -r requirements.txt

COPY . /${APP}/