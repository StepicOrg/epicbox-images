FROM stepik/epicbox-base:stretch
MAINTAINER Pavel Sviderski <ps@stepik.org>

ENV JAVA_INSTALLER_VERSION 9.0.1-1~webupd8~0

# Add Oracle Java 9 (JDK9) repository
RUN apt-get update && apt-get install -y --no-install-recommends gnupg1 \
 && apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys EEA14886 \
 && apt-get purge -y --auto-remove gnupg1 \
 && rm -rf /var/lib/apt/lists/* \
 && echo "deb http://ppa.launchpad.net/webupd8team/java/ubuntu xenial main" | tee /etc/apt/sources.list.d/webupd8team-java.list \
 && echo oracle-java9-installer shared/accepted-oracle-license-v1-1 select true | debconf-set-selections

RUN apt-get update && apt-get install -y --no-install-recommends \
    oracle-java9-installer=${JAVA_INSTALLER_VERSION} \
 && rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk9-installer

COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/local/bin/java_lookup_main.sh
