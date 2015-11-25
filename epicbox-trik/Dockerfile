FROM ubuntu:14.04
MAINTAINER Pavel Sviderski <ps@stepic.org>

RUN useradd -M -d /sandbox sandbox
RUN echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main" > \
    /etc/apt/sources.list.d/toolchain-r-test.list \
 && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1E9377A2BA9EF27F \
 && apt-get update \
 && apt-get install -y --no-install-recommends \
    libglib2.0-0 libxext6 libgl1-mesa-glx libstdc++6 unzip libfreetype6 fontconfig libxrender1 \
 && apt-get clean all

ADD trik_checker.tar.gz /
RUN chown -R root:root /trikStudio-checker

