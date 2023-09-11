FROM golang:1.18-alpine

RUN apk add --no-cache python3 openjdk17-jdk curl bash

RUN apk add --no-cache python3-dev py3-pip gcc musl-dev linux-headers && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v10.0.1.tar.gz && \
    apk del --no-cache python3-dev py3-pip gcc musl-dev linux-headers

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.9.10/kotlin-compiler-1.9.10.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v10.0.3/hs-test-10.0.3.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

WORKDIR /checker

COPY go.mod /checker/

RUN go mod download

COPY checker /checker/

WORKDIR /go
