#! /usr/bin/python

import sys,re

previousline=""
for line in sys.stdin:
	"""line=re.sub("[\n]+","",line)"""
	line= line.strip()
	if line!=previousline:
		previousline=line
		print line
	else:
		continue