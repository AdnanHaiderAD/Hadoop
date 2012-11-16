#! /usr/bin/python

import sys

lineCount=0
wordCount=0
for line in sys.stdin:
	linenum, wordnum =line.split('\t',1)# extracts key and value 
	lineCount= lineCount+int(linenum)
	wordCount= wordCount+int(wordnum)
print'%s\t%s' % (lineCount,wordCount)	
