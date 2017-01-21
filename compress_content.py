#!/usr/bin/env python

import os
import commands as c
import argparse

parser = argparse.ArgumentParser(description='Compress Content')
parser.add_argument('-f','--filter', help='Only compresses by file extension',action="store")
parser.add_argument('-p','--password', help='Password',action="store",required=True)
args = parser.parse_args()

def compress(target):
	
	name,ext = os.path.splitext(target)
	tgz = ''.join([name,'.tgz'])
	zippings = ''.join([name,'.zip'])

	print('--[ Compressing %s' % target) 
	cmd = 'tar cvzf %s %s' % (tgz,target)
	print c.getoutput(cmd)

	cmd = 'zip -P %s %s %s' % (args.password,zippings,tgz)
	print c.getoutput(cmd)

	os.remove(tgz)

	return True	

targets = [n for n in os.listdir(os.getcwd()) if os.path.isfile(n)]
if args.filter:
	targets = [n for n in targets if n.endswith(args.filter)]
for n in targets:
	compress(n)
