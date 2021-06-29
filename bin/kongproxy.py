import os
import shutil

rez = os.listdir('.')
startframe = rez[0].split('.')[1]
rawname = 'kong.%04d.jpg'
outputname = 'Level %s ' % os.getcwd().split()[-1]
targetdir = r'C:\Users\normal\Desktop\Stacking Kong'

os.system('ffmpeg -start_number %s -i %s "%s h264".mov' % (startframe, rawname, outputname))
os.system('ffmpeg -start_number %s -i %s -c:v prores_ks -profile:v 3 "%s.mov"' % (startframe, rawname, outputname))

os.system('mv Level* "%s"' % targetdir)
