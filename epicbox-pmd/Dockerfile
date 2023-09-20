FROM openjdk:8u181-alpine

ENV PMD_VERSION 6.9.0
ENV PATH /opt/pmd/bin:$PATH

RUN apk --no-cache add bash wget unzip && \
    mkdir -p /opt/pmd && \
    wget -O /tmp/pmd.zip "https://github.com/pmd/pmd/releases/download/pmd_releases%2F$PMD_VERSION/pmd-bin-$PMD_VERSION.zip" && \
    unzip /tmp/pmd.zip -d /tmp && \
    cp -R /tmp/pmd-bin-$PMD_VERSION/* /opt/pmd && \
    rm /tmp/pmd.zip && \
    rm -rf /tmp/pmd-bin-$PMD_VERSION && \
    apk del wget unzip

RUN addgroup -g 1000 -S pmd && \
    adduser -u 1000 -S pmd -G pmd
