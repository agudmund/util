#!/usr/bin/env python
# -*- coding: utf-8 -*-

from steganography.steganography import Steganography
import os

def encrypt(root_path,count=0,text=''):
	targets = os.listdir(root_path)
	for word in text.split():
		for n in word:
			target = targets[count]
			path = os.path.join(root, target)
			output_path = os.path.join('/tmp', target)
			Steganography.encode(path, output_path, n)
			count += 1

def decrypt(root_path):

	targets=os.listdir(root_path)
	for n in targets:
		target=os.path.join(root_path,n)
		print (Steganography.decode(target)),
