#!/bin/bash

if [[ -d /home/gradle/.gradle_cache ]]; then
    mv /home/gradle/.gradle_cache/* /home/gradle/.gradle
    rm -rf /home/gradle/.gradle_cache
fi

cp -R /sandbox/. /checker/sandbox/files
gradle test -q --project-dir=/checker/sandbox --no-daemon --console=plain --offline > stdout.txt 2> stderr.txt
echo $? > code.txt
python3 /checker/process.py
