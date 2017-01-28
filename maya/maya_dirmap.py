#!/usr/bin/env mayapy

# Converts Maya data from one directory structure to another ( linux to Windows and so forth )


import sys
import argparse
import maya.cmds as cmds

parser = argparse.ArgumentParser(description='Path converter')
parser.add_argument('--file', help='File',action="store",required=True)
parser.add_argument('--source', help='Path to convert',action="store",required=True)
parser.add_argument('--target', help='Path to convert to',action="store",required=True)

args = parser.parse_args()

cmds.file(args.file, open=True)

cmds.dirmap(en=True)
cmds.dirmap(m=[args.source,args.target])
cmds.dirmap(cd=cmds.getAttr('%s.fileTextureName'%node))

cmds.file('output:%s'%args.file,rename=True)
cmds.file=(save=True)
