FROM ubuntu:14.04
MAINTAINER Pavel Sviderski <ps@stepic.org>

RUN useradd -M -d /sandbox sandbox
RUN  apt-key adv --keyserver keyserver.ubuntu.com --recv-keys 1E9377A2BA9EF27F \
   &&  apt-key adv --recv-keys --keyserver keyserver.ubuntu.com 10C56D0DE9977759

RUN echo "deb http://ppa.launchpad.net/ubuntu-toolchain-r/test/ubuntu trusty main" > \
    /etc/apt/sources.list.d/toolchain-r-test.list \
   && echo "deb http://ppa.launchpad.net/beineri/opt-qt563-trusty/ubuntu trusty main" > \
    /etc/apt/sources.list.d/opt-qt-trusty.list

RUN  apt-get update
RUN  apt-get install -y --no-install-recommends \
    tar bzip2 xz-utils \
    liblsan0 libubsan0 libharfbuzz0b libproxy1 libglib2.0-0 \
    libxext6 libgl1-mesa-glx libstdc++6 unzip libfreetype6 fontconfig libxrender1 \
    qt56base qt56svg qt56script qt56multimedia \
  && apt-get clean all \
  && locale-gen ru_RU.UTF-8 \
  && /bin/echo -e "/opt/qt56/lib/x86_64-linux-gnu\n/opt/qt56/lib\n" > /etc/ld.so.conf.d/zz_opt_qt.conf \
  && ldconfig
ENV LANG ru_RU.UTF-8
ADD trik_checker.tar.xz /
RUN chown -R root:root /trikStudio-checker
