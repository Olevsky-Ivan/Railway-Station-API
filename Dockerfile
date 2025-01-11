FROM python:3.11-bullseye


WORKDIR /app


RUN adduser \
        --disabled-password \
        --no-create-home \
        django-user

COPY . /app/
RUN pip install -r /app/requirements.txt

