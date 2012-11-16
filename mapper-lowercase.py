#! /usr/bin/python

import sys

for line in sys.stdin:
	line= line.lower()
	print line[:-1]