#!/usr/bin/env python

import os

root = r'%s' % os.getcwd()

for n in os.listdir( root ):
	path = os.path.join( root, n )
	os.chdir( path )
	print ('\n==================\n--[ Repository : %s' % n)
	os.system('git status')