FROM golang:1.21-bullseye

ENV GO111MODULE=on

RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    openjdk-17-jdk \
    curl \
    bash \
    linux-headers-amd64 \
    unzip \
    && pip install aiosmtpd beautifulsoup4 pyyaml \
    && pip install https://github.com/hyperskill/hs-test-python/archive/v11.0.0.tar.gz \
    && apt-get remove -y --purge python3-dev linux-headers-amd64 \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*

RUN mkdir /checker  \
    && curl -L -o /checker/kotlin.zip https://github.com/JetBrains/kotlin/releases/download/v1.9.22/kotlin-compiler-1.9.22.zip  \
    && unzip /checker/kotlin.zip -d /checker  \
    && rm /checker/kotlin.zip  \
    && curl -L -o /checker/hs-test.jar https://github.com/hyperskill/hs-test/releases/download/v11.0.0/hs-test-v11.0.0.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/

WORKDIR /sandbox

RUN go mod init sandbox && \
    go get github.com/PuerkitoBio/goquery@v1.8.1 \
    github.com/gin-gonic/gin@v1.9.1 \
    github.com/jmoiron/sqlx@v1.3.5 \
    github.com/mattn/go-sqlite3@v1.14.20 \
    go.uber.org/zap@v1.26.0 \
    gopkg.in/yaml.v3@v3.0.1 \
    gorm.io/driver/sqlite@v1.5.4 \
    gorm.io/gorm@v1.25.6

WORKDIR /go

RUN mv /sandbox /sandbox_tmp