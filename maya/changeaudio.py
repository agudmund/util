#!/usr/bin/env mayapy
# *-* coding: utf-8 *-*
#
# Randomly applies a new song to MASH and updates the simulation
#      usage: 
#     --[ Pick a random song
#   import {this file} as audio
#   source = audio.gather_audio( {path where the music is kept} )
#   audio.switch(source)
#
#     --[ Switch out to an explicit song
#   import {this file} as audio
#   audio.switch( {your music file} )
#
# -aeVar 2017

import os
import random
import maya.mel
import maya.cmds as m

def gather_audio( path  ):
	'''Returns an array of all audio files found in music library'''
	
	pool = []

	for directory, subdir, files in os.walk( path ):
		for file in files:
			if file.endswith( '.wav' ):
				pool.append( os.path.join( directory, file ) )
			if file.endswith( '.aiff' ):
				pool.append( os.path.join( directory, file ) )
	
	return pool

def switch(source, rnd=True ):
	'''Switches all nodes to a new audio file'''

	if rnd:
		current = random.choice( source )
	else:
		current = source

	# Import the audio or use an existing node
	basename = os.path.splitext(os.path.basename(current))[0]

	if not basename in m.ls(type='audio'):
		audionode = m.file( current, i=True )
	else:
		audionode = [n for n in m.ls(type='audio') if n==basename][0]

	# Switch each node per joint
	for node in m.ls( type='MASH_Audio' ):
		m.setAttr( '%s.filename' % node, current, type='string' )

	# Adjust the time slider range
	duration = int(m.getAttr('%s.duration'%audionode))
	m.playbackOptions(max=duration)
	m.playbackOptions(aet=duration)
	
	# Set the sound to be playable in the time slider
	gPlayBackSlider = maya.mel.eval( '$tmpVar=$gPlayBackSlider' )
	target = os.path.basename( current )[:-4].replace( ' ', '_' )
	m.timeControl( gPlayBackSlider, edit=True, sound=target )

if __name__ == '__main__':
	audiopath = os.getenv('AUDIOPATH')
	source = gather_audio(r'%s'%audiopath)
	switch(source)
