FROM python:3.6.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code

WORKDIR /code

ADD Extract_refactor/config/requirements.txt /code/


RUN pip install --upgrade pip \
    && pip install -r requirements.txt

RUN apt-get update \
    && apt-get install -y tesseract-ocr \
    && apt-get install -y imagemagick \
    && apt-get install -y ghostscript

ADD . /code/





