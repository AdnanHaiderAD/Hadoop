#! /usr/bin/python

import sys

count=0
for line in sys.stdin:
	if count < 20:
		print line[:-1]
		count+=1
	else:
		break		
