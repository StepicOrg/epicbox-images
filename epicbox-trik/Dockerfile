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
    tar bzip2 liblsan0 libubsan0 libharfbuzz0b libproxy1 libglib2.0-0 \
    libxext6 libgl1-mesa-glx libstdc++6 unzip libfreetype6 fontconfig libxrender1 \
    qt55base qt55svg qt55script \
  && apt-get clean all \
  && locale-gen ru_RU.UTF-8 \
  && /bin/echo -e "export LANG=ru_RU.UTF-8\nsource /opt/qt55/bin/qt55-env.sh" >> ~/.bashrc
ADD trik_checker.tar.bz2 /
RUN chown -R root:root /trikStudio-checker
