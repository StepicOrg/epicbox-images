FROM debian:bullseye

ENV GCC_VERSION 10.2.1-1

RUN apt-get update \
  && apt-get install -y --no-install-recommends \
    bash \
    cmake \
    curl \
    gcc=4:${GCC_VERSION} \
    gcc-multilib=4:${GCC_VERSION} \
    g++=4:${GCC_VERSION} \
    make \
    openjdk-17-jdk \
    python3 \
    python3-dev \
    python3-pip \
    unzip \
  && rm -rf /var/lib/apt/lists/* \
  && pip3 install https://github.com/hyperskill/hs-test-python/archive/refs/tags/v11.0.0.tar.gz \
  && mkdir /checker \
  && curl -L -o /checker/kotlin.zip \
    https://github.com/JetBrains/kotlin/releases/download/v1.9.10/kotlin-compiler-1.9.10.zip \
  && unzip /checker/kotlin.zip -d /checker \
  && apt-get remove -y unzip \
  && rm /checker/kotlin.zip \
  && curl -L -o /checker/hs-test.jar \
    https://github.com/hyperskill/hs-test/releases/download/v11.0.0/hs-test-v11.0.0.jar

ENV PATH="/checker/kotlinc/bin:$PATH"

COPY checker /checker/
