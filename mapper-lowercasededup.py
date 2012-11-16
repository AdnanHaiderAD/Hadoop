#! /usr/bin/python

import sys,re

uniqlines=set()
for line in sys.stdin:
	"""line=re.sub("[\n]+","",line)"""
	line=line.strip()
	if line not in uniqlines: 
		uniqlines.add(line)
		print line
	else:
		continue
