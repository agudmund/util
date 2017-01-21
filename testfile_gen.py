#!/usr/bin/env python
#
# Basic test file generator (mac only)
# Usage: ./testfile_gen.py

import os

if not os.path.exists("testfiles"):
	os.mkdir("testfiles")

sizes = [ 1, 5, 10, 50, 100 ]
units = [ 'k', 'm', 'g' ]

for unit in units:
	for size in sizes:
		data = {'current':''.join([str(size),unit]).zfill(4)}
		print "--[ Creating Test file: %(current)s" % data
		os.system( "mkfile -n %(current)s testfiles/%(current)s.testfile" % data )

print 'All done, files are in a subdirectory called "testfiles"'