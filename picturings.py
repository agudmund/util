#!/usr/bin/env python

import os
import cv2
import time
import numpy
import shutil

def tile(img):

	raw = cv2.imread(img)
	h=[(n,n+99) for n in xrange(0,720,100)]
	w=[(n,n+99) for n in xrange(0,1200,100)]
	for n in h:
		for x in w:
			cv2.imwrite('sample/__sample_%s%s.png'%(n,x),raw[n[0]:n[1],x[0]:x[1],:])


def diff(last,current,targetdir='sample',threshold=20):

	if not os.path.exists(targetdir):
		os.makedirs(targetdir)

	detect = True
	last = cv2.cvtColor(last,cv2.COLOR_BGR2RGB)
	current = cv2.cvtColor(current,cv2.COLOR_BGR2RGB)

	h=[(n,n+99) for n in xrange(0,720,100)]
	w=[(n,n+99) for n in xrange(0,1200,100)]
	for n in h:
		for x in w:
			sample_one = last[n[0]:n[1],x[0]:x[1],:]
			sample_two = current[n[0]:n[1],x[0]:x[1],:]

			if int(numpy.mean(sample_one))-int(numpy.mean(sample_two))<-threshold:
				if detect:
					target = '%s/spot_%s.jpg'%(targetdir,time.time())
					cv2.imwrite(target,current)
					detect=False

def snip():
	video = cv2.VideoCapture()
	video.open(0)
	ret,image = video.read()
	video.release()

	return image

def watch_for_change(cur=None,last=None):

	while True:
		if cur!=None:
			last = cur
		cur = snip()
		time.sleep(1)

		if last!=None:
			diff(last,cur)

def finder_banner(cur=None,last=None):
	'''Continously updates 10 photos in a folder, because, well, somebody has to animate Finder.'''

	ct = 0

	while True:
		print ct
		
		cur = snip()
		cv2.imwrite('sample/00.jpg',cur)

		try:
			shutil.copy('sample/09.jpg','sample/10.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/08.jpg','sample/09.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/07.jpg','sample/08.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/06.jpg','sample/07.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/05.jpg','sample/06.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/04.jpg','sample/05.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/03.jpg','sample/04.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/02.jpg','sample/03.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/01.jpg','sample/02.jpg' )
		except IOError as e:
			print
		try:
			shutil.copy('sample/00.jpg','sample/01.jpg' )
		except IOError as e:
			print

		ct +=1
		if ct>10:
			ct = 0
			

