FROM golang:1.18-alpine

RUN apk add --no-cache python3

RUN apk add --no-cache python3-dev py3-pip gcc musl-dev linux-headers && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v9.tar.gz && \
    apk del --no-cache python3-dev py3-pip gcc musl-dev linux-headers

COPY checker /checker/
