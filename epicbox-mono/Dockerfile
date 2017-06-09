FROM stepik/epicbox-base:jessie
MAINTAINER Alexander Petrov <alexander.petrov@stepik.org>

ENV MONO_VERSION 5.0.0.100

RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys 3FA7E0328081BFF6A14DA29AA6A19B38D3D831EF

RUN echo "deb http://download.mono-project.com/repo/debian jessie/snapshots/$MONO_VERSION main" > /etc/apt/sources.list.d/mono-official.list && \
    apt-get update && \
    apt-get install -y mono-devel --no-install-recommends && \
    rm -rf /var/lib/apt/lists/* /tmp/*
