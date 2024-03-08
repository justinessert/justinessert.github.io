#!/bin/bash

BRANCH=$(git rev-parse --abbrev-ref HEAD)

for file in img/mascot/*
do
    if [ -f "$file" ]; then
        echo "git add $file"
        git add $file
        git commit -m "added $file"
        git push origin $BRANCH
    fi
done