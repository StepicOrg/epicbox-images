FROM stepik/epicbox-base:trixie
MAINTAINER Stepik Team <team@stepik.org>

ARG DEBIAN_FRONTEND=noninteractive

ENV LUA_VERSION 5.4.7-1+b2

RUN apt-get update && apt-get install -y --no-install-recommends \
    lua5.4=${LUA_VERSION} \
    && rm -rf /var/lib/apt/lists/*
