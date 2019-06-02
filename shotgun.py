#!/usr/bin/env C:/Python27/python.exe

import os
import sys
import random
import json

import shotgun_api3

SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

proj = sys.argv[-1]

class Shotgun:
	def __init__(self):
		self.name = "Fun with a Shotgun"
		self.sg = self.initSG()
		self.projectdir = os.getenv("project")		
		self.projects = self.sg.find('Project',[],['name',"id"])
		self.localprojects = os.listdir(self.projectdir)

	def initSG(self):
		SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
		SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
		SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

		return shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)

	def listProjects(self):
		for n in self.projects:
			print(n['name'])

	def compareProjects(self):

		exixtsinboth = []
		onlylocal = []
		templates = ['Template Project','Motion Capture Template','Demo: Animation','Demo: Game','Game Template','Film Template','TV Series Template','Demo: Animation with Cuts','Game Outsourcing Template','Demo: Automotive','Automotive Design Template']
		
		for y in self.localprojects:
			if y in [n['name'] for n in self.projects]:
				exixtsinboth.append(y)
			else:
				onlylocal.append(y)

		onlyhosted = [n['name'] for n in self.projects if n['name'] not in exixtsinboth+onlylocal+templates]
		
		return exixtsinboth,onlylocal,onlyhosted,templates

if __name__ == "__main__":
	shotgun = Shotgun()
	shotgun.compareProjects()