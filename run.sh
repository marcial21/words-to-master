#!/bin/bash
filename="debug.log"

if [ -e "$filename" ]; then
    echo "Resetting debug.log..."
    rm "$filename"
fi
python3 -B src/main/python/WordsToMaster.py
