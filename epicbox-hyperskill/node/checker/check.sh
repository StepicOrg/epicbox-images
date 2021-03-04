#!/bin/bash

cp -r /sandbox/. /checker/sandbox
cd /checker/sandbox
node node_modules/jest/bin/jest.js -i test/test.js --json > stdout.txt 2> stderr.txt
echo $? > code.txt
python3.5 /checker/process.py
