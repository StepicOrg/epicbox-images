FROM hyperskill.azurecr.io/epicbox/debian:bullseye

ENV GCC_VERSION 10.2.1-1

RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc=4:${GCC_VERSION} gcc-multilib=4:${GCC_VERSION} g++=4:${GCC_VERSION} \
 && rm -rf /var/lib/apt/lists/*
