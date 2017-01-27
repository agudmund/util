#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import os
import boto
import keyring
import paramiko

class Connect():
	def __init__(self,host='',user='root',keyfile=''):
		self.ssh = paramiko.SSHClient()
		self.host = host
		self.keyfile = keyfile
		self.keyfile_resolve()
		self.ssh.connect(self.host ,username='root',pkey=self.password)
		self.transfer = self.ssh.open_sftp()

	def get_folder(self, target):
		files=[os.path.join(target,n.rstrip('\n')) for n in self.talk('ls %s'%target)]
		for entry in files:
			print '--[ Fetching: %s' % entry
			self.transfer.get(entry, entry)

	def send_folder(self, target):
		try:
			files = [ os.path.join(target,n) for n in os.listdir(target) ]
		except OSError as e:
			print '--[ No such directory: %s' % target
			return

		self.talk("mkdir -p %s"%target)
		for entry in files:
			print "--[ Sending: %s" % entry
			self.transfer.put(entry,entry)

	def talk(self, cmd, user='root'):
		stdin,stdout,stderr = self.ssh.exec_command( cmd )
		
		error = stderr.readlines()
		if error == []:
			return stdout.readlines()	
		else:
			return error
		
	def keyfile_expand(self, keyfile):
		'''Returns a full path to a given keyfile.
			supports:
			  ~ for home directory
			  $ environment variable
		'''
		if keyfile.startswith('~'):
			keyfile = os.path.expanduser( keyfile )
		elif keyfile.startswith('$'):
			keyfile = os.getenv(keyfile)
		
		self.keyfile = keyfile

		return True
		
	def keyfile_resolve(self):

		self.keyfile_expand(self.keyfile)
		self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		self.ssh.load_system_host_keys()
		self.password = paramiko.RSAKey.from_private_key_file(
			self.keyfile,
			password=keyring.get_password('SSH', self.keyfile))

		return True


