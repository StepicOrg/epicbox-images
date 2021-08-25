FROM node:16.7-bullseye-slim

RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

RUN pip3 install https://github.com/hyperskill/hs-test-python/archive/v6.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules

COPY checker/ /checker/
