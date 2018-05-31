#!/usr/bin/env python
# *-* coding:utf-8  *-*
#
#  Shader Minglings, some assembly required
#    -If you don't know how to run this script, you probably shouldn't
#
#  -aeVar, 2018

import os
import sys
import maya.cmds as cmds
import maya.mel as mel
from random import choice,randint

class Shader:
	def __init__( self, path=None ):
		self.name = 'Shader mingling'
		self.sourcepath = path
		self.textures = None
		self.shaders = []

	def assign(self):
		'''Applies a random shader from the pile to a selected object'''

		if not self.shaders:
			self.shaders = cmds.ls(type='lambert')

		mel.eval('hyperShade -assign %s' % choice(self.shaders))

	def cleanName(self,name):
		'''Cleans up dirty names'''

		name = os.path.splitext( name )[0]

		for c in  [ '-', '_', '.' ]:
			name = name.replace( c, '' )

		return name

	def createShader(self, texture, shadertype='lambert', alpha=True, prefix=''):
		'''Creates a shader from texture file'''

		fullpath = os.path.join(self.sourcepath,texture)
		texname = '%s%s' % ( prefix, self.cleanName( texture ) )

		print >> sys.__stdout__, 'Creating shader: %s' % texname

		# Create the file node
		fileNode = cmds.createNode( 'file', name='%s_fileTexture' % texname )
		cmds.setAttr('%s.fileTextureName'%fileNode,fullpath,type='string')

		# Create the shading group
		shadingGroup = cmds.sets( name='%s_SG' % texname, empty=True, renderable=True, noSurfaceShader=True )

		# Create the shader, and connect the file node
		shader = cmds.shadingNode( shadertype, name="_".join([ texname, shadertype ]), asShader=True )
		self.shaders.append( shader )
		cmds.connectAttr( '%s.outColor' % shader, '%s.surfaceShader' % shadingGroup)
		cmds.connectAttr( '%s.outColor'%fileNode,'%s.color' % shader )
		if alpha:
			cmds.connectAttr( '%s.outTransparency'%fileNode, '%s.transparency' % shader, f=True )

		return True

	def gatherTextures(self, filetype='.tif' ):
		'''Gathers textures from source path'''

		files = []

		if not self.sourcepath:
			self.pickPath()

		for n in  os.listdir(self.sourcepath):
			if n.endswith(filetype):
				files.append(n)

		self.textures = files

		return files

	def createGeometry(self,shadertype='lambert',prefix='all'):
		'''Creates Polygonal planes from given shaders'''

		if prefix == 'all':
			targetshaders = cmds.ls( type=shadertype ) 
		else:
			targetshaders = [ n for n in cmds.ls( type=shadertype ) if n.startswith(prefix) ]

		targetshaders.remove('lambert1')


		return

	def iterate( self, prefix='', alpha=True, shadertype='lambert' ):
		'''Goes through the textures and applies action to each'''

		if not self.textures:
			self.gatherTextures()

		for tex in self.textures:
			self.createShader( tex , prefix=prefix, alpha=alpha, shadertype=shadertype )

	def pickPath(self):
		'''Folder selector'''

		directory = cmds.fileDialog2(dialogStyle=1, caption='Select a folder with textures',fm=3)
		self.sourcepath = directory[0]
		
		return directory[0]
