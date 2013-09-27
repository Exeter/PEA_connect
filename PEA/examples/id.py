from PEA import users
import json

def pprint(x):
	print(json.dumps(x, indent=4, sort_keys=True))


u = users(by="employeeID")
def getEmailByEmployeeID(employeeid):
	user = u.get(employeeid)
	if not user:
		raise Exception('user not found')
	return user['WorkEmail']
def getNameByEmployeeID(employeeid):
	user = u.get(employeeid)
	if not user:
		raise Exception('user not found')
	first = user['FirstName']
	last = user['LastName']
	return first + ' ' + last

def query():
	try:
		employeeid = str(raw_input('employeeID: '))
		print(getNameByEmployeeID(employeeid))
		print(getEmailByEmployeeID(employeeid))
	except Exception:
		print('user not found')

if __name__ == '__main__':
	while True:
		query()
