#!/bin/bash

for file in mascot/img/*
do
    if [ -f "$file" ]; then
        echo "git add $file"
        git add $file
        git commit -m "added $file"
        git push origin mascot-formatting
    fi
done