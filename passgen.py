#!/usr/bin/env python
#
# Usage: ./passgen.py -n {Length of password}
#        ./passgen.py -n 12

import sys
import random
import string
import argparse

parser = argparse.ArgumentParser(description='Password generator')
parser.add_argument('-n', type=int,
                    help='Length of Password',action="store")
args = parser.parse_args()
if not args.n:
	print parser.print_help()
	sys.exit(1)

symbols = [string.digits,string.letters,string.punctuation]

password = ""

while len(password)!=int(args.n):
	seed = random.choice(symbols[random.randint(0,2)])
	if seed in [ '|', '>', '<','^','\'', '(', ')', '{', '}', '[', ']' ]:
		continue
	else:
		password += seed

print password