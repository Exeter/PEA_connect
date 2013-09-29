#PEA-data-tools
Tools for working with PEA data!

The purpose of these tools is to make PEA data more accessible for student developers; to facilitate students in creating applications useful and relevant to the PEA community.

These tools organize and make public data more accessible for student developers; all of the information gathered by PEA-data-tools can be found on official Academy websites under ordinary usage.

##python module
Facillitates retrieval of Exeter Connect user data. 
Requires [suds](https://fedorahosted.org/suds/)

Here's a basic example:
```python
from PEA import users

user = users().get("slee2")
print("Hello, " + user.get("FirstName") + " " + user.get("LastName"))
```

####PEA.users([<i>by</i>])

 - Returns a dict of all user profiles.

 - *by* specifies the type of key. *by* defaults to ```"Username"```

 - Valid key types: ```"Username"```, ```"EmployeeID"```, ```"UserProfile_GUID"```
 - Example usage:
	```python
	from PEA import users

	byUsername = users()
	byID = users(by="EmployeeID")

	a = byUsername.get('slee2')
	b = byID.get('0704298')
	assert a == b	#True
	```

####PEA.classes([<i>by</i>])
 - Returns a dict of all class profiles.

 - *by* specifies the type of key. *by* defaults to ```"FullString"```

 - Valid key types: ```"FullString"```, ```"ClassCode"```, ``"ClassID"```
 - Example usage:
	```python
	from PEA import classes

	byFullString = classes()
	byClassCode = classes(by="ClassCode")
	
	a = byFullString.get("13/FA Selected Topics * (MAT-590-A)#/classes/mat-590-a-cs81877")
	b = byClassCode.get("mat-590-a")
	assert a == b	#True
	```
	
####PEA.data




Check out the examples at `PEA/examples` for more examples
###javascript module


##Goals:
 - api for python
 - api for javascript
 - user data bindings
 - schedule/calendar bindings
 - authentication bindings

##Todo:
 - Rename this repo PEA-connect-tools
 - Make separate PEA.js repository
 - Make PEA-data-tools website on ECC
 - Implement fromecc methods for data retrieval
