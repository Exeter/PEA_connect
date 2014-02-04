from PEA_connect import data

def _classes():
	original = data.getClassData
	default_type = "FullString"
	other_key_types = ['ClassCode', 'ClassID']
	def classes(by=default_type):
		if by == default_type:
			return original()
		else:
			if by not in other_key_types:
				raise Exception('Invalid key type')
			return dict((v[by],v) for k,v in original().iteritems())

	return classes
def _users():
	original = data.getDetailedUserData
	default_type = "Username"
	other_key_types = ['EmployeeID', 'UserProfile_GUID']
	def users(by=default_type):
		if by == default_type:
			return original()
		else:
			if by not in other_key_types:
				raise Exception('Invalid key type')
			return dict((v[by],v) for k,v in original().iteritems())
	return users
classes = _classes()
users = _users()


