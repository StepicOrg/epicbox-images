FROM python:3.10-slim

RUN apt-get update && \
    apt-get install --yes bc && \
    rm -rf /var/lib/apt/lists/*

RUN pip install https://github.com/hyperskill/hs-test-python/archive/v9.tar.gz

COPY checker/ /checker/
