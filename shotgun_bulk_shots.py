 #!/usr/bin/env python

import os
import random
import shotgun_api3 as shotgun

SERVER_PATH = os.getenv("SHOTGUN_SERVER_PATH")
SCRIPT_USER = os.getenv("SHOTGUN_SCRIPT_USER")
SCRIPT_KEY = os.getenv("SHOTGUN_SCRIPT_KEY")

sg = shotgun.Shotgun(SERVER_PATH, SCRIPT_USER, SCRIPT_KEY)

thumbpath = os.getcwd()
thumbs = [ n for n in os.listdir(thumbpath) if n.endswith('.jpg')]


for i in thumbs:

	print "Creating shot"
	num = os.path.splitext(i)[0][-4:]

	data = {
	    'project': {"type":"Project","id": 86},
	    'code': num,
	    'description': '',
	    'sg_status_list': 'ip'
}

	result = sg.create('Shot', data)
	print result['id'],num

	sg.upload_thumbnail('Shot', result['id'], os.path.join(thumbpath,i) )
