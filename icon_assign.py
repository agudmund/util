#!/usr/bin/env python

# Usage: ./icon.py -f file -i icon.png

import Cocoa
import argparse

def assign(file,icon):
	space = Cocoa.NSWorkspace.sharedWorkspace()
	space.setIcon_forFile_options_(Cocoa.NSImage.alloc().initWithContentsOfFile_(file), icon,0)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Batch icon assign for Mac OS')
	parser.add_argument('-f','--file', help='File to treat',action="store")
	parser.add_argument('-i','--icon', help='Icon to assign',action="store")
	args = parser.parse_args()