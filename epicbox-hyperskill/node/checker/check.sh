#!/bin/bash

cp -r /sandbox/. /checker/sandbox
cd /checker/sandbox
npm test > stdout.txt 2> stderr.txt
echo $? > code.txt
python3.5 /checker/process.py
