#!/bin/bash

cd /sandbox/test
python tests.py --inside_docker > ../stdout.txt 2> ../stderr.txt
echo $? > ../code.txt
python /checker/process.py
