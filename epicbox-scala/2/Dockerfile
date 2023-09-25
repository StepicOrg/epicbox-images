FROM openjdk:8u342-slim

ENV SCALA_VERSION 2.13.12
ENV PATH /opt/scala-$SCALA_VERSION/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget && \
    rm -rf /var/lib/apt/lists/* && \
    touch /usr/local/openjdk-8/release && \
    wget -O - https://downloads.lightbend.com/scala/$SCALA_VERSION/scala-$SCALA_VERSION.tgz | tar xfz - -C /opt

COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/local/bin/java_lookup_main.sh

RUN useradd -M -d /sandbox sandbox
