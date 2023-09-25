FROM bitnami/minideb:bullseye

RUN install_packages \
  curl \
  locales \
  && sed -i -e 's/# en_US.UTF-8 UTF-8/en_US.UTF-8 UTF-8/' /etc/locale.gen \
  && locale-gen

ENV LANG en_US.UTF-8

RUN useradd -M -d /sandbox sandbox
