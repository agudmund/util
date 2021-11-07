#!/usr/bin/env C:\Python27\python

import sockings
import socket
import random
import Leap
import sys

c = sockings.Connect()

class SampleListener(Leap.Listener):

	def on_connect(self, controller):
		print "Connected"
		self.finger_start = 0

	def on_frame(self, controller):

		frame = controller.frame()
		
		for hand in frame.hands:

			if hand.is_right:

				# for finger in hand.fingers:
				# 	if finger.is_extended:
				# 		print '%sFingerbang\n' % '\t'*random.randint(0, 3)

				if hand.confidence == 1:
					c.send( 'setAttr "RightHand.X" %s' % hand.palm_position.x )
					seedling = 0+float(hand.palm_position.y)/100
					c.send( 'setAttr "RightHand.Y" %s' % str(seedling) )
					c.send( 'setAttr "RightHand.Z" %s' % hand.palm_position.z )

					c.send( 'setAttr "RightHand.DirectionX" %s' % hand.direction.x )
					c.send( 'setAttr "RightHand.DirectionY" %s' % hand.direction.y )
					c.send( 'setAttr "RightHand.DirectionZ" %s' % hand.direction.z )

					c.send( 'setAttr "RightHand.Yaw" %s' % hand.direction.yaw )
					c.send( 'setAttr "RightHand.Roll" %s' % hand.palm_normal.roll )

					c.send( 'setAttr "RightHand.Grab" %s' % hand.grab_strength )
					c.send( 'setAttr "RightHand.Pinch" %s' % hand.pinch_strength )
					
			else:
				if hand.confidence == 1:
					c.send( 'setAttr "LeftHand.X" %s' % hand.palm_position.x )
					seedling = 0+float(hand.palm_position.y)/100
					c.send( 'setAttr "LeftHand.Y" %s' % str(seedling) )
					c.send( 'setAttr "LeftHand.Z" %s' % hand.palm_position.z )

					c.send( 'setAttr "LeftHand.DirectionX" %s' % hand.direction.x )
					c.send( 'setAttr "LeftHand.DirectionY" %s' % hand.direction.y )
					c.send( 'setAttr "LeftHand.DirectionZ" %s' % hand.direction.z )

					c.send( 'setAttr "LeftHand.Yaw" %s' % hand.direction.yaw )
					c.send( 'setAttr "LeftHand.Roll" %s' % hand.palm_normal.roll )

					c.send( 'setAttr "LeftHand.Grab" %s' % hand.grab_strength )
					c.send( 'setAttr "LeftHand.Pinch" %s' % hand.pinch_strength )
					

y = ['bone', 'direction',  'is_extended', 'is_finger', 'is_tool', 'is_valid', 'joint_position', 'length', 'stabilized_tip_position', 'this', 'time_visible', 'tip_position', 'tip_velocity', 'touch_distance', 'touch_zone', 'type', 'width']

listener = SampleListener()
controller = Leap.Controller()
controller.add_listener(listener)

print "Press Enter to quit..."
try:
	sys.stdin.readline()
except KeyboardInterrupt:
	pass
finally:
	controller.remove_listener(listener)
