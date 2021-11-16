FROM stepik/epicbox-base:stretch
MAINTAINER Stepik Team <team@stepik.org>

ENV VALGRIND_VERSION 3.12.0~svn20160714-1+b1

RUN apt-get update && apt-get install -y --no-install-recommends \
    valgrind=1:${VALGRIND_VERSION} \
 && rm -rf /var/lib/apt/lists/*
