#! /usr/bin/python

import sys
book =dict([])#data structure that tallies up counts of three-word sequences
for line in sys.stdin:
	#removing non-alphanumeric strings	
	line= ' '.join(word for word in line.split() if word.isalnum())
	wordlist= line.split()#using the white space chacracter to segment the string
	for index,word in enumerate(wordlist):
		if index < len(wordlist)-2:
			seq ='%s' % (' '.join([wordlist[index],wordlist[index+1],wordlist[index+2]]))# creating three-word sequences
			if book.has_key(seq):
				book[seq]= book[seq]+1
			else:
				book[seq]= 1
			
		else:
			break
	
		
for key,value in book.iteritems():	
	print '%s\t%s' % (key, value)
		
