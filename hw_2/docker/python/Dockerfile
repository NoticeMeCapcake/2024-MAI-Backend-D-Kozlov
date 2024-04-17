FROM python:3.9

RUN apt-get update
RUN apt-get install apache2-utils

COPY ./application /application

WORKDIR /application

RUN pip install -r ./requirements.txt

EXPOSE 8000
ENTRYPOINT [ "gunicorn", "--bind", "0.0.0.0:8000", "--workers=1", "main:app"]