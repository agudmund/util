#!/usr/bin/env mayapy
# *-* coding:utf-8 *-*
#
#    Applies blink to a 3D Rig
#   Timing is based off natural blinking patterns of a human
#     ranges 65-85 frames at 24 fps
#
#  Usage:
#     import blinkings as b
#     b.apply_blink()
#
#   -aeVar

import random
import maya.cmds as m
from random import randint
from maya.cmds import playbackOptions

def pick_frame(slider=True):
	'''Returns frames based on time slider or full range for character blinking
		-based on 65-85 frame intervales which is the human average blinking rate
			: slider = Bases the range off the Timeslider, false means it will apply it to the full animation range
	'''

	blink_frames = []
	rate = random.randint( 65, 85 )

	count = 0
	if slider:
		start = int( playbackOptions( min=True, q=True ))
		end = int( playbackOptions( max=True, q=True ))
	else:
		start = int( playbackOptions( ast=True, q=True ))
		end = int( playbackOptions( aet=True, q=True ))

	for i in xrange( start, end ):
		count += 1
		if count == rate:
			blink_frames.append( i )
			rate = randint( 65, 85 )
			count = 0

	return blink_frames

def monicleBlink( frame, offset=0):
	'''
	Applies a blink to a one eyed rig
	  : frame = frame to start the blink on
	  : offset = value offset if the controller is larger or smaller than normal
	'''

	seed = randint(1,5)

	ctrl = 	{
			'single' : 'robot_Eye_Ctrl', # Eye Controller rotate
			'ctrl' : 'rz' # Rotation axis
			}

	m.setKeyframe( ctrl['single'], t=frame-seed, at=ctrl['ctrl'], v=0 )
	m.setKeyframe( ctrl['single'], t=frame, at=ctrl['ctrl'],v=-180 + offset )
	m.setKeyframe( ctrl['single'], t=frame+seed, at=ctrl['ctrl'], v=0 )

	return True

def blink( frame, offset=0 ):
	'''
	Applies a blink to the eye controllers of a rig
	  : frame = frame to start the blink on
	  : offset = value offset if the controller is larger or smaller than normal
	'''

	seed = randint(1,5)

	ctrl = 	{
				'left': 'Normal_ctrlFK_Lf_Eye', # Left Eye Controller
				'right': 'Normal_ctrlFK_Rt_Eye', # Right Eye Controller 
				'up': 'upLidUD', # Upper Eyelid Attribute
				'down': 'loLidUD' # Lower Eyelid Attribute
			}
	
	m.setKeyframe( ctrl['left'], t=frame-seed, at=ctrl['up'], v=0 )
	m.setKeyframe( ctrl['left'], t=frame-seed, at=ctrl['down'], v=0 )
	m.setKeyframe( ctrl['right'], t=frame-seed, at=ctrl['up'], v=0 )
	m.setKeyframe( ctrl['right'], t=frame-seed, at=ctrl['down'], v=0 )

	m.setKeyframe( ctrl['left'], t=frame, at=ctrl['up'],v=4.65 + offset )
	m.setKeyframe( ctrl['left'], t=frame, at=ctrl['down'],v=-3.37 + offset )
	m.setKeyframe( ctrl['right'], t=frame, at=ctrl['up'],v=4.65 + offset )
	m.setKeyframe( ctrl['right'], t=frame, at=ctrl['down'],v=-3.37 + offset )

	m.setKeyframe( ctrl['left'], t=frame+seed, at=ctrl['up'], v=0 )
	m.setKeyframe( ctrl['left'], t=frame+seed, at=ctrl['down'], v=0 )
	m.setKeyframe( ctrl['right'], t=frame+seed, at=ctrl['up'], v=0 )
	m.setKeyframe( ctrl['right'], t=frame+seed, at=ctrl['down'], v=0 )

	return True

def apply_blink(monicle=False):
	'''
	  Main procedure to run, collects frames and applies them to the rig
	'''

	frames = pick_frame()
	for frame in frames:
		if monicle:
			monicleBlink(frame)
		else:
			blink( frame )

	return True

if __name__ == '__main__':
	apply_blink()