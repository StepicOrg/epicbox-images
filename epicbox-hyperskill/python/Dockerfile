FROM python:3.7.3-slim-stretch

RUN apt-get update && \
    apt-get install --yes wget && \
    wget -O hstest.tar.gz https://github.com/hyperskill/hs-test-python/archive/v2.tar.gz && \
    tar -xzvf hstest.tar.gz && \
    mv hs-test* hstest && \
    pip install -e /hstest && \
    rm hstest.tar.gz && \
    apt-get remove --auto-remove --yes wget && \
    rm -rf /var/lib/apt/lists/*

COPY checker/ /checker/
