#!/usr/bin/python
import sys

def mapper():
    for line in sys.stdin:
        data = line.strip().split(',')
        if data[0] == 'URI':
            continue
        if len(data) != 41:
            continue
        
        text = data[2].split()
        for word in text:
            print "{0}\t{1}".format(word, 1)

if __name__ == "__main__":
    mapper()