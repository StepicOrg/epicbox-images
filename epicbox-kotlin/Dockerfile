FROM openjdk:23-slim

ARG COMPILER_URL=https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip
ARG KOTLINX_ATOMICFU_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/atomicfu-jvm/0.25.0/atomicfu-jvm-0.25.0.jar
ARG KOTLINX_CLI_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-cli-jvm/0.3.6/kotlinx-cli-jvm-0.3.6.jar
ARG KOTLINX_DATETIME_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-datetime-jvm/0.6.0/kotlinx-datetime-jvm-0.6.0.jar
ARG KOTLINX_HTML_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-html-jvm/0.11.0/kotlinx-html-jvm-0.11.0.jar
ARG KOTLINX_SERIALIZATION_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-core-jvm/1.7.1/kotlinx-serialization-core-jvm-1.7.1.jar
ARG KOTLINX_SERIALIZATION_JSON_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-json-jvm/1.7.1/kotlinx-serialization-json-jvm-1.7.1.jar

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends wget unzip libfreetype6 fontconfig && \
    rm -rf /var/lib/apt/lists/* && \
    cd /usr/lib && \
    wget -q $COMPILER_URL && \
    unzip kotlin-compiler-*.zip && \
    rm kotlin-compiler-*.zip && \
    rm -f kotlinc/bin/*.bat && \
    cd /usr/lib/kotlinc/lib && \
    wget -q $KOTLINX_ATOMICFU_JVM_URL && \
    wget -q $KOTLINX_CLI_JVM_URL && \
    wget -q $KOTLINX_DATETIME_JVM_URL && \
    wget -q $KOTLINX_HTML_JVM_URL && \
    wget -q $KOTLINX_SERIALIZATION_JVM_URL && \
    wget -q $KOTLINX_SERIALIZATION_JSON_JVM_URL && \
    apt-get remove -y wget unzip && \
    apt-get autoremove -y && \
    apt-get clean -y && \
    rm -rf /var/lib/apt/lists/*

ENV PATH $PATH:/usr/lib/kotlinc/bin

COPY kotlinc /usr/lib/kotlinc/bin/kotlinc
COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/lib/kotlinc/bin/kotlinc /usr/local/bin/java_lookup_main.sh

RUN useradd -M -d /sandbox sandbox

CMD ["kotlinc"]
