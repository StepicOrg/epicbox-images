#!/bin/bash

cd /sandbox
python tests.py > stdout.txt 2> stderr.txt
echo $? > code.txt
python /checker/process.py
