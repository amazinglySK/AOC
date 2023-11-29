#!/bin/bash
echo "making $1"
mkdir "$1"
cd "$1"
touch main.py sample-input.txt input.txt

echo "

f = input('File name : ')
with open(f) as inp_file : 
	# Do something
	pass

" >> main.py
