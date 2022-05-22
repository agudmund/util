#!/usr/bin/env python

# A Very Basic Clip Library Exporter
#    -aeVar 2022

import sys
from pytube import YouTube

class Thingie:
	def __init__(self):
		self.output_path=r'C:\Users\normal\Downloads'
		self.url = r'%s'%sys.argv[-1]
		self.video = self.parse_url()
		self.streams = self.get_streams()

	def parse_url(self):
		'''Chops the url so I don't have to keep cutting it'''

		url = self.url.split('&')[0]
		#url = ''.join(self.url.split('&')[0:1])
		print(url)
		return YouTube( url )

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
						continue

		return thongs

if __name__ == '__main__':
	thing = Thingie()
	print('yay!')

	try:
		thing.video.streams.filter(subtype='mp4' ).get_by_itag(thing.streams[0].itag).download(output_path=r'%s'%thing.output_path)
	except NameError as e:
		print("\n\t--> Could not find higher rez, sorry!\n")
		thing.video.streams.filter(subtype='mp4' )[0].download(output_path=r'%s'%thing.output_path)
	except IndexError as e:
		thing.video.streams.filter(subtype='mp4' )[0].download(output_path=r'%s'%thing.output_path)

	print('Your video is here: %s ' % thing.output_path )
