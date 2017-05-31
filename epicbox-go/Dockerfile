FROM stepik/epicbox-base:alpine-3.6
MAINTAINER Alexander Petrov <alexander.petrov@stepik.org>

RUN set -eux; \
	apk add --no-cache --virtual .build-deps \
		gcc=6.3.0-r4 \
		musl-dev=1.1.16-r9 \
		go=1.8.1-r0

RUN export PATH="/usr/local/go/bin:$PATH";
