FROM haskell:8.8.4
MAINTAINER Stepik Team <ab@stepik.org>

RUN cabal update && \
    cabal install --global --lib random lens mtl transformers parsec split
