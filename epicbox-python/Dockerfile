FROM python:3.10.2
MAINTAINER Alexey Kotenko <alexey.kotenko@stepik.org>

RUN apt update && apt install -y libgeos-dev

COPY ./requirements.txt /home
WORKDIR /home

RUN pip install -r requirements.txt
