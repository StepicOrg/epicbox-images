FROM ubuntu:14.04
MAINTAINER Pavel Sviderski <ps@stepic.org>

RUN useradd -M -d /sandbox sandbox
RUN echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main" > \
    /etc/apt/sources.list.d/toolchain-r-test.list \
   && echo "deb http://ppa.launchpad.net/beineri/opt-qt551-trusty/ubuntu trusty main" > \
    /etc/apt/sources.list.d/opt-qt551-trusty.list \
   && apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1E9377A2BA9EF27F \
   &&  apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 10C56D0DE9977759 \
   && apt-get update \
   && apt-get install -y --no-install-recommends \
    tar bzip2 xz-utils \
    liblsan0 libubsan0 libharfbuzz0b libproxy1 libglib2.0-0 \
    libxext6 libgl1-mesa-glx libstdc++6 unzip libfreetype6 fontconfig libxrender1 \
    qt55base qt55svg qt55script qt55multimedia \
  && apt-get clean all \
  && locale-gen ru_RU.UTF-8 \
  && /bin/echo -e "/opt/qt55/lib/x86_64-linux-gnu\n/opt/qt55/lib\n" > /etc/ld.so.conf.d/zz_opt_qt55.conf \
  && ldconfig
ENV LANG ru_RU.UTF-8
ADD trik_checker.tar.xz /
RUN chown -R root:root /trikStudio-checker
