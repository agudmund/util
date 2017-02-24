#!/usr/bin/env python

import Leap
import time
import cv2
import sys

time.sleep(15)
class SampleListener(Leap.Listener):

	def on_connect(self, controller):
		print "Connected"


	def on_frame(self, controller):

		start = time.time()
		video.open(0)
		while True:
			ret,image = video.read()
			cv2.imwrite('test_%s.png'%time.time(),image)
			time.sleep(1)
			if time.time() - start > 1:
				break
		video.release()

listener = SampleListener()
controller = Leap.Controller()
controller.add_listener(listener)
video = cv2.VideoCapture()

print "Press Enter to quit..."
try:
	sys.stdin.readline()
except KeyboardInterrupt:
	pass
finally:
	controller.remove_listener(listener)

