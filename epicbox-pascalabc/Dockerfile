FROM stepik/epicbox-mono:5.0.0
MAINTAINER Alexander Petrov <alexander.petrov@stepik.org>

RUN apt-get update && apt-get install wget unzip -y &&\
    wget http://pascalabc.net/downloads/PABCNETC.zip -O /tmp/PABCNETC.zip &&\
    mkdir /opt/pabcnetc &&\
    unzip /tmp/PABCNETC.zip -d /opt/pabcnetc &&\
    apt-get --purge remove wget unzip -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/*
