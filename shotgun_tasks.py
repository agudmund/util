#!/usr/bin/env C:/Python27/python.exe

import os
import sys
import random
import json

import shotgun_api3

SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

sg = shotgun_api3.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)
proj = sys.argv[-1]
