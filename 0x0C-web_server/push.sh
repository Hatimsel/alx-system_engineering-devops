#!/bin/bash

read -p 'Commit message: ' commit

git add .
git commit -m "$commit"
git push
