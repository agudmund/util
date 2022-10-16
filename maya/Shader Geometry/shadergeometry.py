#!/usr/bin/env python

import os
import random
import string

from maya import cmds
from maya import mel
from maya import OpenMayaUI as omui 

from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import xml.etree.ElementTree as xml
from shiboken2 import wrapInstance 
from cStringIO import StringIO

import shaders as sh

def loadUiType(uiFile):
    '''Loads a Designer .ui File'''
    import pyside2uic

    parsed = xml.parse(uiFile)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text

    with open(uiFile, 'r') as f:
        o = StringIO()
        frame = {}

        pyside2uic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        form_class = frame['Ui_%s'%form_class]
        base_class = eval(widget_class)
    
    return form_class, base_class

def getTopWindow():
    '''Gets maya top window'''
    import maya.OpenMayaUI as apiUI

    ptr = apiUI.MQtUtil.mainWindow()
    if ptr is not None:
        return shiboken2.wrapInstance(long(ptr), QMainWindow)
    else:
        print "No window found"

uiFile = r'C:\Users\normal\Projects\robot-milagroso\Code\shadergeometry.ui'
pform, pbase = loadUiType(uiFile)

class ShaderMinglings(pform, pbase):
    def __init__(self, parent=None):
        super(ShaderMinglings, self).__init__(parent)

        self.shader = sh.Shader()

        self.setupUi(self)
        self.show()
        self.BTNrootpath.clicked.connect(self.BTNrootpath_onClicked)
        self.BTNfilter.clicked.connect(self.BTNfilter_onClicked)
        self.BTNlambert.clicked.connect(self.BTNlambert_onClicked)
        self.BTNgeometry.clicked.connect(self.BTNgeometry_onClicked)
        self.listings.currentItemChanged.connect(self.listChange)
        self.recent.currentIndexChanged.connect(self.pickRecent)
        self.populateRecent()

    def BTNfilter_onClicked(self):
        '''Filters the results'''
        self.shader = sh.Shader( path = str(self.LBLrootpath.text()))
        
        selected_extension = self.CMBfiletype.itemText(self.CMBfiletype.currentIndex())

        textures = self.shader.gatherTextures()
        self.shader.textures = [n for n in textures if n.endswith(selected_extension)]
        self.listings.clear()
        self.listings.addItems(self.shader.textures)

    def BTNgeometry_onClicked(self):
        '''Creates Polygonal planes from given shaders'''
        self.shader.createGeometry( shadertype=self.shadertype.currentText() , prefix=self.prefix.text() )

    def getRes(self, filename):
        '''Creates a temp file node and grabs the resolution of the target image'''
        name = ''.join([random.choice(string.letters[:26]) for n in range(32)])
        
        mel.eval('createNode file -name %s' % name)
        cmds.setAttr( '%s.fileTextureName'%name, filename, type='string')
        height = int( cmds.getAttr( '%s.outSizeX'%name ))
        width = int( cmds.getAttr( '%s.outSizeY'%name ))
        cmds.delete( name )

        return width,height

    def listChange(self):
        '''Changes the preview icon when the list selection changes'''
        try:
            selected = os.path.join(self.LBLrootpath.text(),self.listings.currentItem().text())
        except:
            return
        selected = selected.replace('/','\\')

        sizeX,sizeY = self.getRes(selected)

        self.picLabel.setScaledContents(True)
        self.picLabel.setPixmap(QPixmap(selected))

    def pickRecent(self):
        path = self.recent.currentText()
        self.LBLrootpath.setText( path )
        self.populateExtensions( path )
        self.BTNtextures_onClicked()

    def populateRecent(self):
        tempdir = os.getenv('TEMP')
        tempfile = os.path.join(tempdir, 'shaderpathRecentlog.txt')
        if os.path.exists(tempfile):
            with open(tempfile) as data:
                rez = data.readlines()
        else:
        	rez = []
        for n in rez:
            self.recent.addItem(n.rstrip('\n'))

    def addToRecent(self, path):

        tempdir = os.getenv('TEMP')
        tempfile = os.path.join(tempdir, 'shaderpathRecentlog.txt')
        
        if os.path.exists(tempfile):
            with open(tempfile, 'a') as data:
                data.write('%s\n'%path)
        else:
            with open(tempfile, 'w') as data:
                data.write('%s\n'%path)

        self.recent.addItem(path)

        return
    
    def BTNlambert_onClicked(self):
        '''Creates the shaders'''
        self.shader.iterate( prefix = self.prefix.text(), alpha = self.transparency.isChecked(), shadertype=self.shadertype.currentText() )

    def populateExtensions(self, path):
        extensions = []
        for n in os.listdir( path ):
            target = os.path.join( path, n )
            self.picLabel.setScaledContents(True)
            self.picLabel.setPixmap(QPixmap(target))
            if os.path.isfile(target):
                name,ext = os.path.splitext( target )
                if ext not in extensions:
                    extensions.append(ext)

        self.CMBfiletype.clear()
        self.listings.clear()
        self.CMBfiletype.addItems( extensions )
        
    def BTNrootpath_onClicked(self):
        '''Picks a new root path'''

        path = self.shader.pickPath()
        self.addToRecent(path)

        self.LBLrootpath.setText( path )
        self.addToRecent( path )
        self.BTNtextures_onClicked()

    def BTNtextures_onClicked(self):
        '''Gathers the textures into a list'''
        self.shader = sh.Shader( path = str(self.LBLrootpath.text()))
        
        selected_extension = self.CMBfiletype.itemText(self.CMBfiletype.currentIndex())

        textures = self.shader.gatherTextures()
        self.listings.clear()
        self.listings.addItems(textures)

if __name__ == '__main__':
    ShaderMinglings()
