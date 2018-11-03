#!/bin/bash
# Grep *.class files in the given directory to find one with psvm method defined
# Usage: java_lookup_main.sh DIRECTORY_PATH

PSVM_REGEX="public static( final)? void main\(java\.lang\.String(\[\]|\.\.\.)\)"

shopt -s nullglob
for f in "$1"/*.class; do
    if javap -p "$f" 2> /dev/null | grep -Pq "$PSVM_REGEX"; then
        filename=$(basename "$f")
        echo -n "${filename%.*}"
        exit 0
    fi
done
exit 1
