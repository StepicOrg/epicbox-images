FROM python:3.12.9-slim-bookworm AS builder

RUN apt-get update && apt-get install -y --no-install-recommends build-essential git

COPY requirements_fasttext_build.txt fasttext.patch /tmp/

WORKDIR /home

RUN git clone https://github.com/facebookresearch/fastText.git \
    && cd /home/fastText \
    && git switch -c 0.9.2 \
    && patch -p1 < /tmp/fasttext.patch \
    && pip install -r /tmp/requirements_fasttext_build.txt \
    && python setup.py bdist_wheel


FROM python:3.12.9-slim-bookworm
MAINTAINER Stepik Team <team@stepik.org>

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONDONTWRITEBYTECODE=1
ENV NLTK_DIR=/usr/local/nltk_data
ENV MYSTEM_DIR=/usr/local/bin

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    gfortran \
    libblas-dev \
    libbz2-dev \
    libffi-dev \
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
COPY --from=builder /home/fastText/dist/fasttext-0.9.2+stepik.1-cp312-cp312-linux_x86_64.whl /tmp/

RUN pip install --no-cache-dir --root-user-action=ignore -r /tmp/requirements.txt \
    && pip install --no-cache-dir --root-user-action=ignore /tmp/fasttext-0.9.2+stepik.1-cp312-cp312-linux_x86_64.whl \
    && python -m nltk.downloader -d ${NLTK_DIR} averaged_perceptron_tagger brown gutenberg movie_reviews omw-1.4 punkt treebank word2vec_sample wordnet \
    && wget -qO- https://download.cdn.yandex.net/mystem/mystem-3.1-linux-64bit.tar.gz | tar xvz -C ${MYSTEM_DIR} \
    && rm /tmp/requirements.txt \
    && rm -Rf /root/.cache/

RUN useradd -M -d /sandbox sandbox \
    && mkdir /sandbox \
    && chown sandbox:sandbox /sandbox
