FROM openjdk:17-slim

RUN apt-get update && \
    apt-get install --yes python3 unzip curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v2.0.0/kotlin-compiler-2.0.0.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v10.0.3/hs-test-10.0.3.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker/ /checker/
