#!/usr/bin/env python

import sys
from pytube import YouTube

url = r'%s'%sys.argv[-1]
video  = YouTube( url )

video.streams.filter(subtype='mp4').all()[0].download(output_path=r'C:\Users\normal\Downloads')