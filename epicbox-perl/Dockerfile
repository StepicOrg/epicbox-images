FROM hyperskill.azurecr.io/epicbox/debian:bullseye

RUN apk add --no-cache perl=5.24.3-r1 \
 && apk add --no-cache --virtual build-dependencies build-base perl-dev \
 && cpan JSON::XS \
 && rm -rf /root/.cpan \
 && apk del build-dependencies
