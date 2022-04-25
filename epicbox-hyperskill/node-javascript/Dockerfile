FROM node:18-alpine

RUN apk add --no-cache python3

RUN apk add --no-cache python3-dev py3-pip gcc musl-dev linux-headers && \
    pip3 install https://github.com/hyperskill/hs-test-python/archive/v9.tar.gz && \
    apk del --no-cache python3-dev py3-pip gcc musl-dev linux-headers

RUN npm install -g https://github.com/hyperskill/sync-input/archive/v1.tar.gz

ENV NODE_PATH=/usr/local/lib/node_modules

COPY checker/ /checker/
