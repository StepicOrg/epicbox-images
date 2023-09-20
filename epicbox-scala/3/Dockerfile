FROM openjdk:11.0.11-slim

ENV SCALA_VERSION 3.0.0
ENV PATH /opt/scala/bin:$PATH

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget && \
    rm -rf /var/lib/apt/lists/* && \
    wget -O - https://github.com/lampepfl/dotty/releases/download/$SCALA_VERSION/scala3-$SCALA_VERSION.tar.gz | tar xfz - -C /opt && \
    mv /opt/scala3-$SCALA_VERSION /opt/scala

COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/local/bin/java_lookup_main.sh

RUN useradd -M -d /sandbox sandbox
