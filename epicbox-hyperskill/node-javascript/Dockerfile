FROM node:18-alpine

RUN apk add --no-cache python3 openjdk17-jdk curl bash

RUN apk add --no-cache python3-dev py3-pip gcc musl-dev linux-headers && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v9.tar.gz && \
    apk del --no-cache python3-dev py3-pip gcc musl-dev linux-headers

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.6.21/kotlin-compiler-1.6.21.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v9.0.2/hs-test-9.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules

COPY checker/ /checker/
