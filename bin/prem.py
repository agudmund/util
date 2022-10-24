#!/usr/bin/env python

import os
import sys
import pymiere
from pymiere.wrappers import time_from_seconds,edit_clip,time_from_seconds  

#-- Target bin

class Thingaling:
	def __init__(self):
		self.name = 'Thingalings adventures into layers'
		
		self.project = pymiere.objects.app.project
		self.project_name = self.project.name.split('.')[0]

		self.sequence = self.project.activeSequence
		self.sequence_name = self.sequence.name

		self.media = os.getcwd()
		self.clips = None
		self.total_duration = 0

		self.validconnection = self.validate()

	def validate(self):
		'''Verifies the app is actually open and so forth'''

		rez = pymiere.objects.app.isDocumentOpen()
		if rez == True:
			print('--[ Connected to Premiere.')
			print('--[ Current Project:\n\t %s' % self.project_name )
			print('--[ Current Sequence:\n\t %s' % self.sequence_name )
		else:
			print('--[ May be better to actually have the app open.')
		return rez


	def importFiles(self):
		'''Import media from current directory into Premiere'''

		rezult = self.project.importFiles(  
		    [self.media],
		    suppressUI=True,  
		    targetBin=self.project.getInsertionBin(),  
		    importAsNumberedStills=False  )

		root = self.project.rootItem
		self.clips = root.findItemsMatchingMediaPath(
			self.media, 
			ignoreSubclips=False)

		print ('--[ Imported:')
		for n in self.clips:
			print ('\t%s'%n.name)

		return rezult

	def alignTracks(self):
		'''Adds the clips to a sequence and offsets them'''
		timing = 0
		for n in range(len(self.clips)):
			clip = self.sequence.videoTracks[n+1].insertClip(self.clips[n], time_from_seconds(timing))
			timing = timing+2

		self.total_duration = timing + 3

	def stretch(self):
		'''Aligns the  the layers'''

		clips = []

		for track in self.sequence.videoTracks:
			try:
				track.clips[0]
				clips.append(track.clips[0])
			except:
				continue

		print('--[ Adjusting length per clip.')
		for n in clips:
			n.end = time_from_seconds(self.total_duration)  

	def setOpacity(self):
		'''Sets the initial keyframes that get set to all text by default'''

		clips = []

		for track in self.sequence.videoTracks:
			try:
				track.clips[0]
				if track.clips[0].name != 'Blank.png':
					clips.append(track.clips[0])
			except:
				continue

		for c in clips:
			for component in c.components:
				if component.displayName == 'Opacity':
					for prop in component.properties:
						if prop.displayName == 'Opacity':
							prop.setTimeVarying(True)
							prop.addKey(c.inPoint.seconds)
							prop.setValueAtKey(c.inPoint.seconds, 0, True)

							prop.addKey(c.inPoint.seconds+1)
							prop.setValueAtKey(c.inPoint.seconds+1, 100, True)

if __name__ == '__main__':
	thing = Thingaling()
	thing.importFiles()
	thing.alignTracks()
	thing.stretch()
	thing.setOpacity()