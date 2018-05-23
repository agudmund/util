
import os
import sys
import maya.cmds as cmds
import maya.mel as mel
from random import choice

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

	def createLambert(self, texture, alpha=True, prefix=''):
		'''Creates a Lamber shader from texture file'''

		fullpath = os.path.join(self.sourcepath,texture)
		texname = '%s%s' % ( prefix, self.cleanName( texture ) )

		print >> sys.__stdout__, 'Creating shader: %s' % texname

		# Create the file node
		fileNode = cmds.createNode( 'file', name='%s_fileTexture' % texname )
		cmds.setAttr('%s.fileTextureName'%fileNode,fullpath,type='string')

		# Create the shading group
		shadingGroup = cmds.sets( name='%s_SG' % texname, empty=True, renderable=True, noSurfaceShader=True )

		# Create the shader, and connect the file node
		shader = cmds.shadingNode( 'lambert', name="%s_lambert" % texname, asShader=True )
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

	def iterate( self, prefix='' ):
		'''Goes through the textures and applies action to each'''

		if not self.textures:
			self.gatherTextures()

		for tex in self.textures:
			self.createLambert( tex , prefix=prefix )

	def pickPath(self):
		'''Folder selector'''

		directory = cmds.fileDialog2(dialogStyle=1, caption='Select a folder with textures',fm=3)
		self.sourcepath = directory[0]
		
		return directory[0]
