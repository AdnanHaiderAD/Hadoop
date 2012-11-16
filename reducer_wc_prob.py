#! /usr/bin/python
import sys,random
counter=0
random.seed(random.randint(1,1000))
for line in sys.stdin:
	count=1
	if random.random()< pow(2,-counter):# if random number generated < b^(-f) where b =2 then increment the  counter by 1
		counter+=1
		
	else:
		continue
print counter
		

