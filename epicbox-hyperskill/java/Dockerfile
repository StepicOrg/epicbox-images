FROM hyperskill.azurecr.io/eclipse-temurin:25-jdk-noble

RUN apt-get update && \
    apt-get install --yes python3 unzip curl && \
    rm -rf /var/lib/apt/lists/*

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v2.3.0/kotlin-compiler-2.3.0.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -fL -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v13.1.0/hs-test-13.1.0.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker/ /checker/
