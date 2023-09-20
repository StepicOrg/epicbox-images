FROM hyperskill.azurecr.io/epicbox/debian:bullseye

ENV VERSION 2.14-1

RUN apt-get update && apt-get install -y --no-install-recommends nasm=${VERSION} binutils \
    && rm -rf /var/lib/apt/lists/*
