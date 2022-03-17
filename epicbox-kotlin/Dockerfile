FROM openjdk:11.0.11-slim
MAINTAINER Stepik Team <team@stepik.org>

ARG COMPILER_URL=https://github.com/JetBrains/kotlin/releases/download/v1.5.31/kotlin-compiler-1.5.31.zip
ARG KOTLINX_DATETIME_JVM_URL=https://repo1.maven.org/maven2/org/jetbrains/kotlinx/kotlinx-datetime-jvm/0.3.2/kotlinx-datetime-jvm-0.3.2.jar

RUN apt-get update && apt-get install -y --no-install-recommends wget unzip \
    libfreetype6 fontconfig && \
    rm -rf /var/lib/apt/lists/* && \
    cd /usr/lib && \
    wget -q $COMPILER_URL && \
    unzip kotlin-compiler-*.zip && \
    rm kotlin-compiler-*.zip && \
    rm -f kotlinc/bin/*.bat && \
    cd /usr/lib/kotlinc/lib && \
    wget -q $KOTLINX_DATETIME_JVM_URL && \
    apt-get remove -y wget unzip && \
    apt-get autoremove -y && \
    apt-get autoclean -y

ENV PATH $PATH:/usr/lib/kotlinc/bin

COPY kotlinc /usr/lib/kotlinc/bin/kotlinc
COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/lib/kotlinc/bin/kotlinc /usr/local/bin/java_lookup_main.sh

RUN useradd -M -d /sandbox sandbox

CMD ["kotlinc"]
