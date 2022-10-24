#!/usr/bin/env python

import os,shutil
from time import sleep



files = os.listdir(os.getcwd())

filter01 = ['Turbo-Octo-Kitten---Page-04', 'Page 04 Body 05 - ']
filter02 = ['_',' ']
filter03 = ['-',' ']
filter04 = ['  ',' ']
y='Page 04 Body 05    0000s 0002 0'

for n in files:
	print(n)
	x = n.replace(filter01[0],filter01[1])
	x = x.replace(filter02[0],filter02[1])
	x = x.replace(filter03[0],filter03[1])
	x = x.replace(x[:len(y)], filter01[1])
	print(x)
	shutil.move(n,x)

