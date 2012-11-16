#! /usr/bin/python

import sys

prev_Seq=""
counter=0
for line in sys.stdin:
	
	seq,count =line.strip().split('\t',1);#extract key and value
	count=int(count)
	if prev_Seq==seq:
		counter=counter+count
	else:
		if prev_Seq!="":
			print '%s\t%s' % (prev_Seq,counter)# print three word sequence and it corresponding total count
		prev_Seq=seq
		counter=count	
print '%s\t%s' % (prev_Seq,counter)
