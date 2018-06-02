#!/usr/bin/env C:\Python27\python.exe

import sys

import os
import random
import string

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import xml.etree.ElementTree as xml
from shiboken2 import wrapInstance 
from cStringIO import StringIO

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

uiFile = 'testui.ui'
pform, pbase = loadUiType(uiFile)



class Tester(pform, pbase):
	def __init__(self, parent=None):
		super(Tester, self).__init__(parent)

		self.setupUi(self)
		
		self.rootpath = r'C:\Users\normal\Projects'

		self.populateProjects()

		self.projects.currentItemChanged.connect(self.desc)

		self.setWindowIcon(QIcon(r'C:\Users\normal\Projects\util\tray\Icons\Icon.png'))
		self.show()

	def desc(self):

		things = os.path.join(self.rootpath,self.projects.currentItem().text(),'10 Things.txt')

		rez = ['']

		if os.path.exists(things):
			with open(things) as data:
				rez = data.readlines()

		self.labelTest.setText(''.join(rez))

	def populateProjects(self):
		self.projects.addItems(os.listdir(self.rootpath))


app = QApplication(sys.argv)
t = Tester()
sys.exit(app.exec_())