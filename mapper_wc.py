#! /usr/bin/python

import sys,re

for line in sys.stdin:
	#removing non-alphanumeric characters
	line= ' '.join(word for word in line.split() if word.isalnum())
	words= line.split()#segmenting the line into a list of words using the whitespace character
	numberOfWords=len(words)
	print '%s\t%s' % (1,numberOfWords) # key =1(mapper has currently seen 1 line) and value= number of words in the line.
