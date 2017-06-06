FROM stepik/epicbox-monocs:5.0
MAINTAINER Alexander Petrov <alexander.petrov@stepik.org>

RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates unzip &&\
        wget http://pascalabc.net/downloads/PABCNETC.zip -O /tmp/PABCNETC.zip &&\
        mkdir /usr/bin/pabcnetc &&\
        unzip /tmp/PABCNETC.zip -d /usr/bin/pabcnetc &&\
        apk del build-dependencies &&\
        rm /tmp/*
