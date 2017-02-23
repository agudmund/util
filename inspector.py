import sys
import inspect

# Usage: {within a python script}
# import inspector
# inspector.listen() {will print to stdout all occurrences of said action}

def listen():
	curframe = inspect.currentframe()
	calframe = inspect.getouterframes(curframe, 2)
	print >> sys.__stdout__,'caller name:', calframe[1][1], calframe[1][3]
