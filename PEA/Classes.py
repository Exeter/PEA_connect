from . import data
from copy import deepcopy
# Convenience methods for working with class data

by_fullstring = data.getClassData()
def byFullString(*args):
	if len(args) == 0:
		return deepcopy(by_fullstring)
	elif len(args) == 1:
		return by_fullstring.get(args[0])
	else:
		output = {}
		for fullstring in args:
			try:
				output[fullstring] = by_fullstring[fullstring]
			except:
				pass
		return output
