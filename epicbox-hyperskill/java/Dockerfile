FROM adoptopenjdk:16

RUN apt-get update && \
    apt-get install --yes python3 unzip && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.5.0/kotlin-compiler-1.5.0.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v8.1/hs-test-8.1.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker/ /checker/
