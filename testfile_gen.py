#!/usr/bin/env python
#
# Basic test file generator (mac only)
# Usage:  ./testfile_gen.py -p {path to generate the test files in}
#         ./testfile_gen.py -p targetpath

import os
import sys
import platform
import argparse

def create_files(sizes = [ 1, 5, 10, 50, 100 ], units = [ 'K', 'M', 'G' ]):
	'''Creates test files of given sizes'''

	for unit in units:
		for size in sizes:
			data = {'current':''.join([str(size),unit]).zfill(4),'path':args.path}
			print "--[ Creating Test file: %(current)s" % data
			if platform.system() == 'Darwin':
				os.system( "mkfile -n %(current)s %(path)s/%(current)s.testfile" % data )
			elif platform.system() == 'Linux':
				os.system('fallocate -l %(current)s %(path)s/%(current)s.testfile' % data)
			else:
				print 'Unsupported OS'

	return True

def validate_path(path):
	'''Validates and creates a target path'''

	if not os.path.exists(args.path):

		os.mkdir(args.path)
		return True
	else:
		print 'Path already exists, overwrite? (Y/N)'
		if raw_input() in ['y','Y']:
			return True
		else:
			return False


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Test file generator')
	parser.add_argument('-p','--path', type=str,help='Target path to place the files in',action="store",required=True)
	args = parser.parse_args()

	if validate_path(args.path):
		create_files()
		print 'All done, files are in a subdirectory called "%s"'% args.path