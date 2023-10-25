FROM python:3.11.5-slim


ENV DEBIAN_FRONTEND=noninteractive
ENV NLTK_DIR=/usr/local/nltk_data
ENV MYSTEM_DIR=/usr/local/bin

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    gfortran \
    libblas-dev \
    libbz2-dev \
    libfreetype6-dev \
    libgdbm-dev \
    libgeos-dev \
    libjpeg-dev \
    liblapack-dev \
    liblzma-dev \
    libncursesw5-dev \
    libreadline-dev \
    libsqlite3-dev \
    libssl-dev \
    libxml2-dev \
    libxslt-dev \
    libz-dev \
    locales \
    pkg-config \
    uuid-dev \
    wget \
    zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && sed -i '/\(en_US.UTF-8\|ru_RU.UTF-8\)/s/^# //g' /etc/locale.gen \
    && locale-gen

COPY requirements.txt /tmp

RUN pip install --no-cache-dir -r /tmp/requirements.txt \
    && python -m nltk.downloader -d ${NLTK_DIR} averaged_perceptron_tagger brown gutenberg movie_reviews omw-1.4 punkt treebank word2vec_sample wordnet \
    && wget -qO- https://download.cdn.yandex.net/mystem/mystem-3.1-linux-64bit.tar.gz | tar xvz -C ${MYSTEM_DIR} \
    && rm /tmp/requirements.txt

RUN useradd -M -d /sandbox sandbox \
    && mkdir /sandbox \
    && chown sandbox:sandbox /sandbox
