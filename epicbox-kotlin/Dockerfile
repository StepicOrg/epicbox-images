FROM eclipse-temurin:11-jdk-jammy
MAINTAINER Stepik Team <team@stepik.org>

ARG COMPILER_URL=https://github.com/JetBrains/kotlin/releases/download/v2.3.20/kotlin-compiler-2.3.20.zip
ARG KOTLINX_ATOMICFU_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/atomicfu-jvm/0.27.0/atomicfu-jvm-0.27.0.jar
ARG KOTLINX_CLI_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-cli-jvm/0.3.6/kotlinx-cli-jvm-0.3.6.jar
ARG KOTLINX_DATETIME_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-datetime-jvm/0.6.2/kotlinx-datetime-jvm-0.6.2.jar
ARG KOTLINX_HTML_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-html-jvm/0.12.0/kotlinx-html-jvm-0.12.0.jar
ARG KOTLINX_SERIALIZATION_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-core-jvm/1.8.1/kotlinx-serialization-core-jvm-1.8.1.jar
ARG KOTLINX_SERIALIZATION_JSON_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-serialization-json-jvm/1.8.1/kotlinx-serialization-json-jvm-1.8.1.jar
ARG RETROFIT_URL=https://repo1.maven.org/maven2/com/squareup/retrofit2/retrofit/2.12.0/retrofit-2.12.0.jar
ARG CONVERTER_GSON_URL=https://repo1.maven.org/maven2/com/squareup/retrofit2/converter-gson/2.12.0/converter-gson-2.12.0.jar
ARG OKHTTP_URL=https://repo1.maven.org/maven2/com/squareup/okhttp3/okhttp/4.12.0/okhttp-4.12.0.jar
ARG OKIO_JVM_URL=https://repo1.maven.org/maven2/com/squareup/okio/okio-jvm/3.12.0/okio-jvm-3.12.0.jar
ARG GSON_URL=https://repo1.maven.org/maven2/com/google/code/gson/gson/2.13.1/gson-2.13.1.jar

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
    wget -q $RETROFIT_URL && \
    wget -q $CONVERTER_GSON_URL && \
    wget -q $OKHTTP_URL && \
    wget -q $OKIO_JVM_URL && \
    wget -q $GSON_URL && \
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
