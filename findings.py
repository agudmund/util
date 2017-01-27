#!/usr/bin/env python

import os
import time
import math

import commands as c 


path = ''
exclude = ['.DS_Store']
projects = [ n for n in os.listdir(path) if n not in exclude ]

for project in projects:
	results = {}
	for x,y,z in os.walk(project):
		for n in z:
			if n not in exclude:

				target = os.path.join(x,n)
				dirings = os.path.dirname(target)
				now = time.time()
				mtime = os.stat(target).st_mtime
				
				days_ago = int((((now - mtime)/60)/60)/24) #days ago
				results[dirings]=days_ago
				results[dirings]

	try:
		minim = min(results.values())
	except ValueError as e:
		print e
		print project
		print results
	for x in results:
		if minim == results[x]:
			print '%s,%s,%s,'%(x.split('/')[0],results[x],x)

