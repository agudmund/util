#!C:\Program Files\Python36\python

import os
import random

exclude_path = os.path.join(os.getenv("TMP"),"pickit_exclude.tmp")
working_path = os.getenv("project")

if os.path.exists(exclude_path):
	with open(exclude_path) as data:
		rez = data.readlines()
else:
	rez = []

exclude = [n.rstrip('\n') for n in rez]
c = os.listdir(os.getenv("project"))
candidates = [n for n in c if n not in exclude]
candidate = candidates[random.randrange(0,len(candidates))]
exclude.append(candidate)

with open(exclude_path,'w') as data:
	for n in exclude:
		data.write('%s\n'%n)

print(candidate)

if len(c)==len(exclude):
	os.remove(exclude_path)
