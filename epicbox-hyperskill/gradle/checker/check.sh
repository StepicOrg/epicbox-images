#!/bin/bash

cp -R /checker/template/. /sandbox
python3 /checker/prepare_gradle.py
gradle test -q --project-dir=/sandbox --no-daemon --console=plain --offline > stdout.txt 2> stderr.txt
echo $? > code.txt
python3 /checker/process.py
