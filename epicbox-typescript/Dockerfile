FROM node:18.12.0-bullseye-slim

ENV TYPESCRIPT_VERSION=4.8.4
ENV TYPES_NODE_VERSION=18.11.9

RUN useradd -M -d /sandbox sandbox \
    && mkdir /sandbox \
    && chown sandbox:sandbox /sandbox

RUN npm install -g \
    typescript@${TYPESCRIPT_VERSION} \
    @types/node@${TYPES_NODE_VERSION}

WORKDIR /sandbox
