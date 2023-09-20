FROM hyperskill.azurecr.io/epicbox/debian:bullseye

ENV MONO_VERSION 6.10.0.104

RUN apt-get update && \
    apt-get install -y --no-install-recommends gnupg && \
    apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF && \
    echo "deb http://download.mono-project.com/repo/debian buster/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-official.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends mono-devel && \
    rm -rf /var/lib/apt/lists/* /tmp/*
