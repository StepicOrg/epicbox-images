FROM stepik/epicbox-base:stretch
MAINTAINER Pavel Sviderski <ps@stepik.org>

ENV GCC_VERSION 6.3.0-4

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:${GCC_VERSION} gcc-multilib=4:${GCC_VERSION} g++=4:${GCC_VERSION} \
 && rm -rf /var/lib/apt/lists/*
