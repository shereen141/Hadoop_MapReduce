#!/usr/bin/python
import sys


word_count = 0
old_word = None

for line in sys.stdin:
    data = line.strip().split("\t")
    
    if len(data) != 2:
        continue
    
    current_word, value = data
    
    if old_word and old_word != current_word:
        print "{0}\t{1}".format(old_word, word_count)
        word_count = 0
    
    old_word = current_word
    word_count += int(value)

if old_word != None:
    print "{0}\t{1}".format(old_word, word_count)

