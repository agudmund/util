#!/usr/bin/env python
#! *-* coding:utf-8 *-*

import os
import io
import json
import shutil
import random
import webbrowser
import win10toast
import cv2

# Picks out bookmarks from Chrome
# -aeVar 2016

class Bookmarks:
	def __init__(self):

		self.setupEnv()		
		self.source = os.path.join(self.appdata, self.chromeDataPath)
		self.target = os.path.join(self.tmp,"bookmark_export")
		self.links = self.getBookmarks()
		self.urls = self.getUrls()

	def setupEnv(self):
		"""Set up environment for target files"""
		self.appdata = os.getenv("LOCALAPPDATA")
		self.tmp = os.getenv("TMP")
		self.chromeDataPath = os.path.join("Google","Chrome","User Data","Default","Bookmarks")
		self.chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

	def getBookmarks(self):
		"""Read the bookmarks into a dictionary"""
		shutil.copy(self.source, self.target)

		rez = io.open(self.target, 'r', encoding='utf-8')
		bookmarks = json.loads(rez.read())
		rez.close()

		return bookmarks

	def getUrls(self):
		"""Extracts urls from the bookmarks main bar"""
		b = self.links['roots']['bookmark_bar']
		return [n for n in b['children'] if n['type']=='url' if n]

	def pickBookmark(self):
		current = random.choice(b.urls)
		bookmark = (current['name'],current['url'])
		
		msg = "Opening %s at path %s" % (bookmark[0], bookmark[1]) 
		print(msg)
		webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(bookmark[1])

if __name__ == '__main__':
	b = Bookmarks()
	b.pickBookmark()
	