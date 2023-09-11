#!/bin/sh
cp -r /sandbox_tmp/* /sandbox
cd /sandbox
python3 /checker/process.py
