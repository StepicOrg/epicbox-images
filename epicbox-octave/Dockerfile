FROM stepik/epicbox-base:stretch
MAINTAINER Pavel Sviderski <ps@stepik.org>

ENV OCTAVE_VERSION 4.0.3-3
ENV SYMBOLIC_VERSION 2.6.0
# required to locate python for symbolic package
ENV PYTHON /usr/bin/python3

RUN apt-get update && apt-get install -y --no-install-recommends \
    octave=${OCTAVE_VERSION} python3-sympy ca-certificates \
 && rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install -y --no-install-recommends wget \
 && wget https://downloads.sourceforge.net/project/octave/Octave%20Forge%20Packages/Individual%20Package%20Releases/symbolic-${SYMBOLIC_VERSION}.tar.gz \
    -O /tmp/symbolic.tar.gz \
 && octave-cli --quiet --no-window-system --no-history --norc --eval 'pkg install -global /tmp/symbolic.tar.gz' \
 && apt-get purge -y wget \
 && rm -rf /var/lib/apt/lists/* /tmp/*
