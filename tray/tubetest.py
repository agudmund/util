#!/usr/bin/env python

from pytube import YouTube
import sqlite3
import shutil
import os

class Fetch:
	def __init__(self):
		self.set_paths()
		self.refresh_history()

	def set_paths(self):
		'''Sets source and target paths for history file'''

		history = 'Google\Chrome\User Data\Default\History'

		self.source = os.path.join(os.getenv('LOCALAPPDATA'), history)
		self.target = os.path.join(os.getenv('TMP'),'History')

	def refresh_history(self):
		shutil.copy(self.source, self.target)
		self.read_history()

		return True

	def read_history(self):

		if not os.path.exists(self.target):
			self.refresh_history()

		db = sqlite3.connect(self.target)
		c = db.cursor()
		c.execute('SELECT * from urls')
		self.history = c.fetchall()

		self.youtube_history = [n for n in self.history if 'www.youtube.com' in n[1] if 'watch' in n[1]]

	def grab(self,url):

		video = YouTube( url )
		print video.streams.filter(subtype='mp4').all()[0].download()


if __name__ == '__main__':
	tick = Fetch()
	tick.refresh_history()
	tick.read_history()
	for n in tick.youtube_history:
		print n[2]
