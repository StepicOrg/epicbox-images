#!/bin/bash

cd /sandbox
python -m unittest discover -s test > stdout.txt 2> stderr.txt
echo $? > code.txt
python /checker/process.py
