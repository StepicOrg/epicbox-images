FROM bitnami/minideb:bullseye

RUN apt-get update && apt-get install -y --no-install-recommends \
  curl \
  locales \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen && locale-gen

ENV LANG en_US.UTF-8

RUN useradd -M -d /sandbox sandbox
