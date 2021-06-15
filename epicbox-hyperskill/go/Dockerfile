FROM golang:1.16.5-buster

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN pip3 install https://github.com/hyperskill/hs-test-python/archive/v5.tar.gz

COPY checker/ /checker/
