#!/usr/bin/env C:\Python27\python.exe

import sys
from pytube import YouTube

url = r'%s'%sys.argv[-1]
video  = YouTube( url )

video.streams.filter(subtype='mp4').all()[0].download()