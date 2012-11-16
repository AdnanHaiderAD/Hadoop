#! /usr/bin/python
import sys, random
counter=0
prev_Seq=""
seq_counter=0
random.seed(random.randint(1,1000))
for line in sys.stdin:
	seq, count =line.strip().split('\t',1);#extract key and value
	count=int(count)
	if prev_Seq==seq:
		if random.random()<pow(1.2,-counter):# if random number generated < b^(-f) where b =1.2 then increment the current three-word sequence 's count
			counter+=1
			seq_counter=seq_counter+count
		else:
			continue
	else:
		if prev_Seq!="":
			print '%s\t%s' % (prev_Seq,seq_counter)
		prev_Seq=seq
		counter=1
		seq_counter=count
		random.seed(random.randint(1,1000))# initializing the seed of the random number generator for the new sequence

		
			
print '%s\t%s' % (prev_Seq,seq_counter)			
				
