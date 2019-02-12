#!/usr/bin/env python
#! *-* coding:utf-8 *-*

import os
import io
import json
import shutil
import random
import webbrowser
import requests
from lxml import html
import cv2

# Picks out bookmarks from Chrome

def grab_bookmarks():
	'''Convert the bookmark file into readable format'''

	source = os.path.join(os.getenv("LOCALAPPDATA"), 'Google\\Chrome\\User Data\\Default\\Bookmarks')
	target = os.path.join(os.getenv("TMP"),"bookmark_export")

	shutil.copy(source, target)

	rez = io.open(target, 'r', encoding='utf-8')
	bookmarks = json.loads(rez.read())
	rez.close()

	return bookmarks

if __name__ == '__main__':
	bookmarks = grab_bookmarks()
	bookmark_bar = bookmarks['roots']['bookmark_bar']

	urls = [n for n in bookmark_bar['children'] if n['type']=='url' if n]

	current = random.choice(urls)
	print(current['name'],current['url'])
	webbrowser.get("C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s").open(current['url'])
