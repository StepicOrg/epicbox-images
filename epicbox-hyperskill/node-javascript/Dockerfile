FROM node:17.1-slim

RUN apt update && \
    apt install -y --no-install-recommends python3 python3-pip && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v8.tar.gz && \
    apt remove -y --auto-remove python3-pip && \
    rm -rf /var/lib/apt/lists/*

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules

COPY checker/ /checker/
