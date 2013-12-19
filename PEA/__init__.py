from PEA import data
import requests

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


def auth(uname, pword):
	"""
	Returns True if authentication succeeds
	Return False if authentication fails
	"""
	def _webmail_auth(uname, pword):
		"""
		Uses webmail.exeter.edu basic authentication

		Returns True if authentication succeeds
		Return False if authentication fails
		"""
		url = "https://webmail.exeter.edu/exchweb/bin/auth/owaauth.dll"
		payload = {"destination": "https://webmail.exeter.edu/exchange", "username": uname, "password":  pword, "SubmitCreds": "Log On"}
		r = requests.post(url, data=payload)
		if r.url == "https://webmail.exeter.edu/exchange/":
			return True
		return False
	return _webmail_auth(uname,pword)
