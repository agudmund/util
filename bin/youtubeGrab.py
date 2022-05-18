#!/usr/bin/env python

import sys
from pytube import YouTube

class Thingie:
	def __init__(self):
		self.url = r'%s'%sys.argv[-1]
		self.video = YouTube( self.url )
		self.streams = self.get_streams()
		self.output_path=r'C:\Users\normal\Downloads'
		self.itag = self

	def get_streams(self):
		'''Just return a list of what is available'''
		rez = self.video.streams.filter(subtype='mp4')

		thongs = []

		for item in rez:
			if item.type == 'audio':
				continue
			if item.type == 'video':
				if(len(item.resolution))>4:
					if item.video_codec.startswith('avc1'):
						thongs.append(item)
						#itagz = n.itag
						continue

		return thongs

if __name__ == '__main__':
	thing = Thingie()
	print('yay!')

	try:
		thing.video.streams.filter(subtype='mp4' ).get_by_itag(thing.streams[0].itag).download(output_path=r'C:\Users\normal\Downloads')
	except NameError as e:
		print("\n\t--> Could not find higher rez, sorry!\n")
		thing.video.streams.filter(subtype='mp4' )[0].download()

	print('Your video is here: %s ' % thing.output_path )
