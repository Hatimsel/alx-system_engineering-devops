#!/bin/bash

read 'Commit message: ' commit

git add .
git commit -m '$commit'
git push
