FROM python:3.9.6-alpine3.13 as dev

WORKDIR /work

FROM python:3.9.6-alpine3.13 as debugging

FROM dev as runtime
COPY ./src/ /app

ENTRYPOINT ["python", "/app/app.py"]