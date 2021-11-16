FROM stepik/epicbox-base:stretch
MAINTAINER Stepik Team <team@stepik.org>

ENV GCC_VERSION 6.3.0-4
ENV VALGRIND_VERSION 3.12.0~svn20160714-1+b1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:${GCC_VERSION} gcc-multilib=4:${GCC_VERSION} g++=4:${GCC_VERSION} \
    valgrind=1:${VALGRIND_VERSION} \
 && rm -rf /var/lib/apt/lists/*
