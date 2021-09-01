#!/bin/bash

cp -R /sandbox/. /checker/sandbox/files
gradle test -q --project-dir=/checker/sandbox --no-daemon --console=plain --offline > stdout.txt 2> stderr.txt
echo $? > code.txt
python3 /checker/process.py
