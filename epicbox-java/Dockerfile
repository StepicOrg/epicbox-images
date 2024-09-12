FROM openjdk:23-slim

ARG GSON_LIB_URL=https://repo1.maven.org/maven2/com/google/code/gson/gson/2.10.1/gson-2.10.1.jar
ARG JAVAX_JSON_API_LIB_URL=https://repo1.maven.org/maven2/javax/json/javax.json-api/1.1.4/javax.json-api-1.1.4.jar
ARG JAVAX_JSON_LIB_URL=https://repo1.maven.org/maven2/org/glassfish/javax.json/1.1.4/javax.json-1.1.4.jar
ARG JSON_SIMPLE_LIB_URL=https://repo1.maven.org/maven2/com/googlecode/json-simple/json-simple/1.1.1/json-simple-1.1.1.jar

ARG JAVA_LIB_PATH=/usr/local/lib/java

ENV CLASSPATH=.:$JAVA_LIB_PATH/*

RUN mkdir -p $JAVA_LIB_PATH

ADD $GSON_LIB_URL $JAVA_LIB_PATH
ADD $JAVAX_JSON_API_LIB_URL $JAVA_LIB_PATH
ADD $JAVAX_JSON_LIB_URL $JAVA_LIB_PATH
ADD $JSON_SIMPLE_LIB_URL $JAVA_LIB_PATH

RUN chmod og+r $JAVA_LIB_PATH/*

COPY java_lookup_main.sh /usr/local/bin/java_lookup_main.sh
RUN chmod +x /usr/local/bin/java_lookup_main.sh

RUN useradd -M -d /sandbox sandbox
