FROM stepik/epicbox-base:trixie
MAINTAINER Stepik Team <team@stepik.org>

ARG DEBIAN_FRONTEND=noninteractive

ENV GCC_VERSION 4:14.2.0-1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=${GCC_VERSION} gcc-multilib=${GCC_VERSION} g++=${GCC_VERSION} \
    && rm -rf /var/lib/apt/lists/*
