#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import sys
import time
import inspect
import tempfile

class Util:
	def __init__(self):
		self.log_msg = []

	def get_tmp(self):
		
		tmp_dir = os.getenv('TMP')
		if not tmp_dir:
			tmp_dir = '/tmp'
		if not os.path.exists( tmp_dir ):
			try:
				os.mkdir( tmp_dir )
			except OSError as e:
				tmp_dir = os.path.expanduser('~/tmp')

		self.log_msg.append('--[ Using %s as temporary directory' % tmp_dir)

		return tmp_dir

	def log(self, msg):

		c=inspect.currentframe()
		(frame, filename, line_number,
			function_name, lines, index) = inspect.getouterframes(inspect.currentframe())[1]
		callee = filename.split(os.path.sep)[-1]

		self.log_msg.append('[%s] %s'%(filename,msg))
		print >> sys.stderr, r'%s'%msg

		if callee == '<stdin>':
			callee = __name__

		temp_dir = self.get_tmp()
		temp = tempfile.NamedTemporaryFile(prefix='%s.%s'%('logfile-%s'%callee,time.strftime('%y-%m-%d-%H:%M:%S-')),suffix='.log',dir='/tmp',delete=False)
		print temp.name
		for entry in self.log_msg:
			temp.write( '\n%s'%entry )
		temp.write('\n')
		temp.close()

	def thumbs(self):
		thumbs = '''.        __                       __
       (   |                     |   )
  _____ \   \                   /   /_____
 (____ _)    \                /    (_____)
 (_____ )   _)__( •̃͡-̮•̃͡)__(_  (     _____)
 (__ ___)     )   |___|     (   (_ ___)
  (_____)__/    /_/\_\      \__ (____)'''
  		for n in thumbs.split('\n'):
  			print n

	def batch(self,frames, batch):
		'''Returns batches from a list of frames.'''
		return [frames[i:i+batch] for i in range(0, len(frames), batch)]

	def editor(self):
		if os.getenv('EDITOR'):
			editor = os.getenv('EDITOR')
		else:
			if True in ['sublime' in os.listdir(n) for n in os.getenv('PATH').split(':')]:
				editor = 'sublime'
			else:
				editor = None
				print '--[ sublime not found in $PATH, please set $EDITOR to the location of your editor of choice'
		return editor