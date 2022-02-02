FROM python:3.10.2
MAINTAINER Alexey Kotenko <alexey.kotenko@stepik.org>

RUN apt update && apt install -y libgeos-dev

COPY ./requirements.txt /home
WORKDIR /home

ENV NLTK_DIR=/usr/local/nltk_data
ENV MYSTEM_DIR=/usr/local/mystem/

RUN pip install -r requirements.txt
RUN python -m nltk.downloader -d ${NLTK_DIR} averaged_perceptron_tagger brown gutenberg movie_reviews omw-1.4 punkt treebank word2vec_sample wordnet
RUN mkdir -p ${MYSTEM_DIR} && wget -qO- https://download.cdn.yandex.net/mystem/mystem-3.1-linux-64bit.tar.gz | tar xvz -C ${MYSTEM_DIR}
