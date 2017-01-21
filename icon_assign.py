#!/usr/bin/env python

# Usage: ./icon.py file icon.png

import Cocoa
import sys

space = Cocoa.NSWorkspace.sharedWorkspace()
space.setIcon_forFile_options_(Cocoa.NSImage.alloc().initWithContentsOfFile_(sys.argv[1]), sys.argv[2],0)