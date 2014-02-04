from PEA_connect import users

byUsername = users()
byID = users(by="EmployeeID")

a = byUsername.get('slee2')
b = byID.get('0704298')
assert a == b
