from PEA import data
from copy import deepcopy

def _classes():
	original = data.getClassData()
	default_type = "FullString"
	other_key_types = ['ClassCode', 'classID']
	def classes(by=default_type):
		if by == default_type:
			return original
		else:
			if type not in other_key_types:
				raise Exception('Invalid key type')
			return deepcopy(dict((v[by],v) for k,v in original.iteritems()))

	return classes
def _users():
	original = data.getDetailedUserData()
	default_type = "UserName"
	other_key_types = ['employeeID', 'UserProfile_GUID']
	def users(by=default_type):
		if by == default_type:
			return original
		else:
			if by not in other_key_types:
				raise Exception('Invalid key type')
			return deepcopy(dict((v[by],v) for k,v in original.iteritems()))
	return users
classes = _classes()
users = _users()

