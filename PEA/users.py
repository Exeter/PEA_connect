from . import data
from copy import deepcopy
# Convenience methods for working with user data

"""
no arguments       : return whole list of profile
one argument       : return single profile
multiple arguments : return partial list of profiles
"""

by_username = data.getDetailedInfo()
def byUsername(*args):
	if len(args) == 0:
		return deepcopy(by_username)
	elif len(args) == 1:
		return by_username.get(args[0])
	else:
		output = {}
		for username in args:
			try:
				output[username] = by_username[username]
			except:
				pass
		return output


by_employeeid = dict((v['employeeID'],v) for k,v in by_username.iteritems())
def byEmployeeID(*args):
	if len(args) == 0:
		return deepcopy(by_employeeid)
	elif len(args) == 1:
		return by_employeeid.get(args[0])
	else:
		output = {}
		for employeeid in args:
			try:
				output[employeeid] = by_employeeid[employeeid]
			except:
				pass
		return output
