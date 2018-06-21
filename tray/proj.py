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

		self.projects.currentItemChanged.connect(self.projectChange)
		self.resetProgress.clicked.connect(self.milestone)
		self.addstep.clicked.connect(self.clickAddStep)

		self.setWindowIcon(QIcon(r'C:\Users\normal\Projects\util\tray\Icons\Icon.png'))
		self.show()

	def milestone(self):
		'''Milestone reset the selected project'''

		conf = os.path.join(self.rootpath,self.projects.currentItem().text(),'proj.conf')

		if os.path.exists(conf):
			with open(conf) as data:
				rez = data.readlines()

		output = []
		for n in rez:
			if n.startswith('steps'):
				output.append('steps,0')
				continue
			output.append(n)
		
		with open(conf,'w') as data:
			data.write('\n'.join(output))

		self.projectChange()

	def readConf(self, conf):
		if os.path.exists(conf):
			with open(conf) as data:
				rez = data.readlines()

			steps = [n for n in rez if n.startswith('steps')]
			step = int( steps[0].split(',')[-1] )

			return step
		else:
			return 0

	def clickAddStep(self):

		conf = os.path.join(self.rootpath,self.projects.currentItem().text(),'proj.conf')

		if os.path.exists(conf):
			with open(conf) as data:
				rez = data.readlines()

			steps = [n for n in rez if n.startswith('steps')]
			step = int( steps[0].split(',')[-1] )
			step = step+1

			if step>5:
				step = 5

			with open(conf, 'w') as data:
				for line in rez:
					if line.startswith('step'):
						line = 'steps,%s'%step
					data.write('%s\n'%line)

		self.projectChange()

		return True

	def setProgress(self,num):

		self.progress.setValue(num)

	def setColors(self):

		blue = QColor(0,0,255)
		black = QColor(0,0,0)
		orange = QColor(255,140,0)

		for i in range(self.projects.count()):
			conf = os.path.join(self.rootpath,self.projects.item(i).text(),'proj.conf')
			step = self.readConf(conf)

			if step==5:
				self.projects.item(i).setForeground(QBrush(blue))
			elif step==0:
				self.projects.item(i).setForeground(QBrush(black))
			else:
				self.projects.item(i).setForeground(QBrush(orange))
				

		return True

	def projectChange(self):

		things = os.path.join(self.rootpath,self.projects.currentItem().text(),'10 Things.txt')
		conf = os.path.join(self.rootpath,self.projects.currentItem().text(),'proj.conf')

		self.setColors()

		# 10 Things
		rez = ['']
		if os.path.exists(things):
			with open(things) as data:
				rez = data.readlines()
		self.labelTest.setText(''.join(rez[5:]))
		try:
			self.mileItem1.setText(rez[0])
			self.mileItem2.setText(rez[1])
			self.mileItem3.setText(rez[2])
			self.mileItem4.setText(rez[3])
			self.mileItem5.setText(rez[4])
		except IndexError as e:
			print

		step = self.readConf(conf)
		self.progress.setValue( step*20 )

	def populateProjects(self):

		projects = os.listdir(self.rootpath)

		self.projects.addItems( projects )

		self.projects.setCurrentRow(random.randint(0,len(projects)))
		self.projectChange()

app = QApplication(sys.argv)
t = Tester()
sys.exit(app.exec_())