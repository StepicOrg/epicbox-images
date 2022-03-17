#!/bin/bash

cd /sandbox
python3 tests.py --inside_docker > stdout.txt 2> stderr.txt
echo $? > code.txt
python3 /checker/process.py
