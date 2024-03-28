FROM debian:12.5-slim
LABEL maintainer="Stepik Team <team@stepik.org>"

ENV LANG=ru_RU.UTF-8
ENV ONESCRIPT_VERSION=1.8.4
ENV DEBIAN_FRONTEND=noninteractive

RUN apt update && \
    apt-get -y --no-install-recommends install \
    locales \
    tzdata \
    binutils \
    curl \
    mono-runtime \
    ca-certificates \
    ca-certificates-mono \
    mono-fastcgi-server4 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* && \
    sed -i '/\(en_US.UTF-8\|ru_RU.UTF-8\)/s/^# //g' /etc/locale.gen && \
    locale-gen

RUN curl https://oscript.io/downloads/lts/x64/onescript-engine_${ONESCRIPT_VERSION}_all.deb > oscript.deb && \
    dpkg -i oscript.deb && \
    rm -f oscript.deb

RUN useradd -m -d /sandbox sandbox
