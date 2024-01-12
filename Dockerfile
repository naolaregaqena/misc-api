FROM python:3.10.12-slim-bullseye

WORKDIR /usr/local/src/misc-api

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY misc_api ./misc_api

ENV HOST=0.0.0.0
ENV POST=8080

CMD [
    "uvicorn",
    "misc_api.main:main",
    "--factory",
    "--host", "$HOST",
    "--port", "$PORT"
]
