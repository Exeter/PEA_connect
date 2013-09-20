from .. import users
import json

def pprint(x):
	print(json.dumps(x, indent=4, sort_keys=True))


def getEmailByEmployeeID(employeeid):
	user = users.byEmployeeID(employeeid)
	return user['WorkEmail']
def getNameByEmployeeID(employeeid):
	user = users.byEmployeeID(employeeid)
	first = user['FirstName']
	last = user['LastName']
	return first + ' ' + last

def verify(employeeid):
	if not users.byEmployeeID(employeeid):
		return False
	return True

def query():
	employeeid = str(raw_input('EmployeeID: '))
	if not verify(employeeid):
		print("user not found")
		query()
		return
	print(getNameByEmployeeID(employeeid))
	print(getEmailByEmployeeID(employeeid))

if __name__ == '__main__':
	query()
