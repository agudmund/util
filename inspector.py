import sys
import inspect
curframe = inspect.currentframe()
calframe = inspect.getouterframes(curframe, 2)
print >> sys.__stdout__,'setTrgPath----->caller name:', calframe[1][3]
