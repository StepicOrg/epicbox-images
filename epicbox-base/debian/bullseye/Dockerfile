FROM bitnami/minideb:bullseye
MAINTAINER Stepik Team <team@stepik.org>

RUN apt-get update && apt-get install -y --no-install-recommends locales && \
  rm -r /var/lib/apt/lists /var/cache/apt/archives && \
  sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

ENV LANG en_US.UTF-8

RUN useradd -M -d /sandbox sandbox
