#!/usr/bin/env python

import sys
from pytube import YouTube

url = r'%s'%sys.argv[-1]
video  = YouTube( url )


rez = video.streams.filter(subtype='mp4')

for n in rez:
	if n.type == 'video':
		if(len(n.resolution))>4:
			itagz = n.itag
			break
try:
	video.streams.filter(subtype='mp4' ).get_by_itag(itagz).download(output_path=r'C:\Users\normal\Downloads')
except NameError as e:
	print("\n\t--> Could not find higher rez, sorry!\n")
	video.streams.filter(subtype='mp4' ).all()[0].download(output_path=r'C:\Users\normal\Downloads')