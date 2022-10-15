#!/usr/bin/env python

import os
import sys
import random

# Add already selected ones to a list
exclude_path = os.path.join(os.getenv("TMP"),"pickit_exclude.tmp")
if os.path.exists(exclude_path):
	with open(exclude_path) as data:
		rez = data.readlines()
else:
	rez = []

def pickPath():
	### Get Path from environment, if no commandline argument is supplied
	if len(sys.argv)<2:
		working_path = os.getenv("project")
	else:
		working_path = sys.argv[1]

	return working_path

if __name__ == '__main__':

	working_path = pickPath()
	exclude = [n.rstrip('\n') for n in rez]
	c = os.listdir(working_path)
	candidates = [n for n in c if n not in exclude]
	candidate = candidates[random.randrange(0,len(candidates))]
	exclude.append(candidate)

	with open(exclude_path,'w') as data:
		for n in exclude:
			data.write('%s\n'%n)

	print(candidate)

	if len(c)==len(exclude):
		os.remove(exclude_path)
