import sys

path = sys.argv[-1]

with open(path) as data:
	rez = data.readlines()

for n in rez:
	if 'rdi' in n:
		if '$ART_LOCAL' in n:
			print (n.strip('\n').split("ART_LOCAL_ROOT")[-1].split("ASSETS")[-1])
