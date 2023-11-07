FROM ruby:3.2.2-alpine3.18
LABEL maintainer="Stepik Team <team@stepik.org>"

RUN adduser -DH -h /sandbox sandbox

WORKDIR /sandbox

COPY Gemfile Gemfile.lock ./

RUN apk add --no-cache --virtual build-dependencies build-base sqlite-dev make gcc musl-dev && \
    bundle config --global frozen 1 && \
    bundle install && \
    apk del build-dependencies
