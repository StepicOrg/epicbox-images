FROM hyperskill.azurecr.io/epicbox/debian:bullseye

ENV JAVA_INSTALLER_VERSION 9.0.1-1~webupd8~0

# Add Oracle Java 9 (JDK9) repository
RUN add-apt-repository ppa:webupd8team/java \
  && apt-get update && apt-get install -y --no-install-recommends \
    oracle-java9-installer=${JAVA_INSTALLER_VERSION} \
  && rm -rf /var/lib/apt/lists/* /var/cache/oracle-jdk9-installer

COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/local/bin/java_lookup_main.sh
