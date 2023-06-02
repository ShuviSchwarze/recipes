# syntax=docker/dockerfile:1

FROM python:3.10-alpine

WORKDIR /usr/src/api

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt --no-cache-dir

COPY ./entrypoint.sh .
RUN sed -i 's/\r$//g' /usr/src/api/entrypoint.sh
RUN chmod +x /usr/src/api/entrypoint.sh

COPY . .

ENTRYPOINT [ "/usr/src/api/entrypoint.sh" ]
