#!/usr/bin/env python

import cProfile as c

count = 50000000

def strings():

	# 10000003 function calls in 6.070 seconds
	# 100000003 function calls in 73.886 seconds

	things = []

	for i in xrange(count):
		things.append('this %s operation has %s attempts' % ( 'string conversion', str(i).zfill(5) ))

def formats():

	# 15000003 function calls in 7.012 seconds 
	# 150000003 function calls in 80.719 second

	things = []

	for i in xrange(count):
		things.append('this {} operation has {} attempts'.format( 'format', str(i).zfill(5) ))

c.run("strings()")
c.run("formats()")