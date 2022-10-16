#!/usr/bin/env python

import os
import maya.cmds as cmds
import maya.mel as m

def get_images():
	
	images = []

	root = r"C:\Users\normal\Projects\robot-milagroso\Source\Output\Images\012"
	for x,y,z in os.walk(root):
		for n in z:
			name,ext = os.path.splitext(n)

			images.append((name,os.path.join(x,n)))

	return images

def iterate():
	c=0
	previousHeight=0
	previousWidth=0
	cur=0
	offset = 0
	rAlign = 0
	spacer = 0
	maxheight = 0
	heightoffset = 0
	for image in get_images():

		if not('.') in image[0]:
			try:
				name = image[0].replace(' ','_').replace('-','_')
				rez=cmds.polyPlane()

				# Create the shader
				fileNode = '%s_fileTexture' % image[0]
				print name
				SHD = m.eval('shadingNode -asShader -name "%s" lambert ' % name)
				FIL = m.eval('createNode file -name "%s_file"' % name)

				# Connect it
				m.eval('connectAttr %s.outColor %s.color' % ( FIL, SHD ) )
				cmds.setAttr('%s.fileTextureName'%FIL,image[1],type='string')
				cmds.select(rez)
				m.eval('hyperShade -assign %s' % SHD)

				width = cmds.getAttr('%s_file.outSizeX'%name)
				height = cmds.getAttr('%s_file.outSizeY'%name)
				cmds.setAttr('%s.width'%rez[1],width)
				cmds.setAttr('%s.height'%rez[1],height)			

				if height>maxheight:
					maxheight = height

				if previousWidth!=0:
					rAlign = (previousWidth/2) + (width/2)
				
				if offset>1000:
					rAlign = 0
					offset = 0
					if heightoffset==0:
						heightoffset = heightoffset + (maxheight)
					else:
						heightoffset = heightoffset + maxheight 
					maxheight = 0

				cmds.move(rAlign+offset+ spacer,0,heightoffset + (heightoffset/5) + (maxheight/10)) 

				offset = offset + rAlign + spacer
				
				previousWidth = width 
				spacer = width /10

				cmds.rename(rez[0],'%s_GEO'%name)
				cmds.select(clear=True)
			except:
				print("Skipping")
				continue