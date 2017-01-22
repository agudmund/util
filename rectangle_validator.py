#!/bin/env python

import sys
import random

class Rect:
	def __init__(self,point=[1,1],rectangle_size=[5,5]):
		self.x = point[0]
		self.y = point[1]
		self.width = rectangle_size[0]
		self.height = rectangle_size[1]
		self.rect = self.rectangle()

	def rectangle(self ):
		"""Returns a 2D matrix rectangle of a given height and width"""

		rect = [[n for n in xrange( self.width  )] for n in xrange( self.height ) ]

		return rect

	def test(self ):
		"""Validates if a point falls within a matrix"""

		if self.x <= len(self.rect):
			try:
				self.rect[self.y]
				return True
			except IndexError as e:
				return False
		else:
			return False

if __name__ == '__main__':

	print '--[ Running 10 validation tests on a random range'
	for i in xrange(0,10):

		data = {
		'rh' : random.randint(0,20),
		'rw' : random.randint(0,20),
		'x' : random.randint(0,20),
		'y' : random.randint(0,20)
		}

		rect= Rect(point=[data['x'],data['y']],rectangle_size=[data['rh'],data['rw']])

		if rect.test():
			print '\tPoint %(x)s,%(y)s falls within a rectangle of the size [%(rh)s, %(rw)s] ' % data
		else:
			print ' ! Point %(x)s,%(y)s does not fall within a rectangle of the size [%(rh)s, %(rw)s] ' % data
