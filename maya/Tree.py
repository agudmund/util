#!/usr/bin/env python

import maya.cmds as m
import maya.mel as mel
from random import randint,choice,random

###  Happy Trees and friends
###    Creates a bunch of random trees in Maya
###   -aeVar 2022 

class HappyTreeFriends:
	def __init__(self):
		self.name = 'Fun times with Fluff and Honey'
		self.colors =[
				'Tree_Palette_tree_01',
				'Tree_Palette_tree_02',
				'Tree_Palette_tree_03',
				'Tree_Palette_tree_04',
				'Tree_Palette_tree_05'
					]

		self.corebush = 'Tree_Wild_Jungle'
		self.bushvariations = [
				'Tree_Lombardi_Lake',
				'Tree_Atlantic_Ocean',
				'Tree_Bohemian_Earth',
				'Tree_Desert_Vista',
				'Tree_Sedona_Mountain',
				'Tree_Canyon_Blossom',
				'Tree_Succulent'
								]
		self.count = 0
		self.corecount = 0

		self.gridlingx = 0
		self.gridlingz = 0

	def bush(self,min=2,max=5):
		'''Bush thingy'''
		num=randint(min,max)
		for i in range(num):
			name='tree_%s_%s'%(str(self.count).zfill(2),str(i).zfill(2))
			seed = {'height':randint(1,int(max/2)),'radius':randint(5,12)/10.0}
			
			if self.corecount<3:
				currentbush = self.corebush
			else:
				currentbush = choice(self.bushvariations)
				self.corecount = 0
			m.select(currentbush)
			
			m.duplicate(name=name)
			m.move(randint(47,53),randint(8,15),randint(-3,3),absolute=True)
			radius = random()*seed['radius']
			m.scale(seed['radius'],seed['radius'],1,relative=True)
			self.corecount = self.corecount+1

			
	def trunk(self):
		'''Happy little trees stand on stubs'''
		name = 'tree_%s_trunk'%( str(self.count).zfill(2),  )
		
		cub = m.polyCube(name=name)
		m.move(-108,16,-2)
		m.rotate(90,0,0,relative=True)
		mel.eval('hyperShade -assign %s' % 'Tree_Palette_trunk_lambert')

		m.select('%s.f[2]'%name)
		m.scale(random()+1,random()+1,1,relative=True)

		m.select('%s.f[0]'%name)
		m.move(0,-15,0, relative=True)
		m.scale(random()+randint(2,4),random()+randint(2,4),1,relative=True)


	def group(self):
		'''combines the thing'''
		trunksize = randint(3,7)
		m.select('tree_%s*'%str(self.count).zfill(2))
		m.group()
		m.move(self.gridlingx,0,self.gridlingz)
		m.rotate(0,randint(0,365),0)
		self.count = self.count +1
		gridspace = 15
		self.gridlingx = self.gridlingx + gridspace
		if self.gridlingx == gridspace*9:
			self.gridlingx = 0
			self.gridlingz = self.gridlingz  + gridspace




if __name__ == '__main__':
	tree = HappyTreeFriends()
	for i in range(30):
		tree.bush()
		tree.trunk()
		tree.group()