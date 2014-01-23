#PEA_connect
PEA_connect facilitates retrieval of Exeter Connect user data.

All of the information gathered by PEA-data-tools can be found on official Academy websites under ordinary usage methods.

[Examples](PEA_/examples/README.md)

#Easy?
Supports python 2 only.
Requires [suds](https://fedorahosted.org/suds/)
```
pip install suds
```

Here's a basic example:
```python
import PEA_connect

users = PEA_connect.users()

user = users.get(raw_input("Your username please? "))
print("Hello " + user.get("FirstName") + " " + user.get("LastName") + "!")
```

####PEA_connect.users([<i>by</i>])

 - Returns a dict of all user profiles.

 - *by* specifies the type of key. Given no arguments, *by* defaults to ```"Username"```

 - Valid key types: ```"Username"```, ```"EmployeeID"```, ```"UserProfile_GUID"```
 - Example usage:
	```python
	from PEA import users

	byUsername = users()	#users(by="Username")
	byID = users(by="EmployeeID")

	a = byUsername.get('slee2')
	b = byID.get('0704298')
	assert a == b	#True
	```

####PEA_connect.classes([<i>by</i>])
 - Returns a dict of all class profiles.

 - *by* specifies the type of key. *by* defaults to ```"FullString"```

 - Valid key types: ```"FullString"```, ```"ClassCode"```, ``"ClassID"```
 - Example usage:
	```python
	from PEA import classes

	byFullString = classes()	#classes(by="FullString")
	byClassCode = classes(by="ClassCode")
	
	a = byFullString.get("13/FA Selected Topics * (MAT-590-A)#/classes/mat-590-a-cs81877")
	b = byClassCode.get("mat-590-a")
	assert a == b	#True
	```
##Todo:
 - Make PEA-data-tools website on ECC
 - Make changes to code that reflect README
  - simplify to single file, get rid of unnecessary package structure
