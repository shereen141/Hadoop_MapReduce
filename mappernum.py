#!/usr/bin/python

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
	count =0
    line = line.strip()
    line = line.split(",")
    if count <=1:
    	count+=1
    	continue
    if len(line) !=41:
    	continue
    sex = line[21]
    age = line[24]

        print '%s\t%s' % (sex, age)