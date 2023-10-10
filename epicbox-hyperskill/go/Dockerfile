FROM golang:1.18.2-alpine

ENV GO111MODULE=on

RUN apk add --no-cache python3 openjdk17-jdk curl bash

RUN apk add --no-cache python3-dev py3-pip gcc musl-dev linux-headers && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v10.0.2.tar.gz && \
    apk del --no-cache python3-dev py3-pip linux-headers

RUN mkdir /checker && \
    curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.9.10/kotlin-compiler-1.9.10.zip && \
    unzip /checker/kotlin.zip -d /checker && \
    rm /checker/kotlin.zip

RUN curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v10.0.3/hs-test-10.0.3.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/

WORKDIR /sandbox
RUN go mod init sandbox && \
    go get github.com/gin-gonic/gin@v1.8.2 && \
    go get github.com/mattn/go-sqlite3@v1.14.13 && \
    go get github.com/jmoiron/sqlx@v1.3.5 && \
    go get gorm.io/gorm@v1.23.5 && \
    go get gorm.io/driver/sqlite@v1.3.2 && \
    go get go.uber.org/zap@v1.24.0

WORKDIR /go

RUN mv /sandbox /sandbox_tmp
