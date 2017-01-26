#!/usr/bin/env python
#
# Basic test file generator (mac only)
# Usage: ./testfile_gen.py

import os
import argparse

parser = argparse.ArgumentParser(description='Test file generator')
parser.add_argument('-p','--path', type=str,help='Target path to place the files in',action="store",required=True)
args = parser.parse_args()

if not os.path.exists(args.path):
	os.mkdir(args.path)

sizes = [ 1, 5, 10, 50, 100 ]
units = [ 'k', 'm', 'g' ]

for unit in units:
	for size in sizes:
		data = {'current':''.join([str(size),unit]).zfill(4),'path':args.path}
		print "--[ Creating Test file: %(current)s" % data
		os.system( "mkfile -n %(current)s %(path)s/%(current)s.testfile" % data )

print 'All done, files are in a subdirectory called "testfiles"'