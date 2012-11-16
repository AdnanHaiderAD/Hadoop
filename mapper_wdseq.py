#! /usr/bin/python

import sys

for line in sys.stdin:
	#removing non-alphanumeric characters
	line= ' '.join(word for word in line.split() if word.isalnum())
	wordlist= line.split()#using the white space chacracter to segment the string into a list of words
	for index,word in enumerate(wordlist):
		if index < len(wordlist)-2:
			seq ='%s' % (' '.join([wordlist[index],wordlist[index+1],wordlist[index+2]]))# creating three-word sequences
			print '%s\t%s' % (seq,1)
		else:
			break
