#!/bin/bash
echo "making $1"
mkdir "$1"
cd "$1"
touch main.py sample-input.txt input.txt

echo "
import sys

f = sys.argv[1] 
with open(f) as inp_file : 
	pass
" >> main.py
