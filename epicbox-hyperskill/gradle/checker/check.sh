#!/bin/bash

if [[ -d /home/gradle/.gradle_cache ]]; then
    mv /home/gradle/.gradle_cache/* /home/gradle/.gradle
    rm -rf /home/gradle/.gradle_cache
fi

cp -R /checker/template/. /sandbox
gradle test -q --project-dir=/sandbox --console=plain --offline > stdout.txt 2> stderr.txt
echo $? > code.txt
python3 /checker/process.py
