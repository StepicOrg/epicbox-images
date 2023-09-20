FROM stepik/epicbox-mono:6.10.0

RUN apt-get update && apt-get install wget unzip -y &&\
    wget http://pascalabc.net/downloads/PABCNETC.zip -O /tmp/PABCNETC.zip &&\
    mkdir /opt/pabcnetc &&\
    unzip /tmp/PABCNETC.zip -d /opt/pabcnetc &&\
    apt-get --purge remove wget unzip -y &&\
    rm -rf /var/lib/apt/lists/* /tmp/*
