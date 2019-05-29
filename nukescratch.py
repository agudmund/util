import os
import sys
import nuke
import random

inScript = sys.argv[-1]

nuke.scriptOpen( inScript )

body = nuke.toNode('body').knob('file')
write = nuke.toNode('output').knob('file')


rootpath = r'C:/Users/normal/Projects/Reactive/Unity/Assets/Textures/Blankito/0000s_0006_F05_50.044 eyes04'

targets = [os.path.join(rootpath,n) for n in os.path.listdir(rootpath) if n.endswith('exr')]

for n in targets:

	body.setValue(n)
	output.setValue(n.replace('mouth','south'))
	nuke.execute('output',1,1)

###
body = nuke.toNode('body').knob('file')
output = nuke.toNode('output').knob('file')


rootpath = r'C:/Users/normal/Projects/Reactive/Unity/Assets/Textures/Blankito/0000s_0006_F05_50.044 eyes04'

targets = ['%s/%s'%(rootpath,n) for n in os.listdir(rootpath) if n.endswith('exr')]

for n in targets:

    body.setValue(n)
    output.setValue(n.replace('mouth','south').replace('.exr','.tif'))
    nuke.execute('output',1,1)