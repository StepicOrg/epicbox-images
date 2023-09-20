FROM ruby:2.5.3-alpine

RUN adduser -DH -h /sandbox sandbox && \
    apk add --no-cache --virtual build-dependencies build-base && \
    apk add --no-cache sqlite-dev && \
    gem install rspec:3.8.0 sqlite3:1.3.13 sequel:5.15.0 && \
    apk del build-dependencies
