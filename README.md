#PEA-data-tools
Tools for working with PEA data!

PEA-data-tools organize and make public data more accessible for student developers. All of the information gathered by PEA-data-tools can be found on official Academy websites under ordinary usage.

[Examples](PEA/examples/README.md)

##Python module
Facillitates retrieval of Exeter Connect user data. 
Requires [suds](https://fedorahosted.org/suds/)

Here's a basic example:
```python
from PEA import users

print("Hello World!")
print("Just kidding. What kind of name is World??")
user = users().get(raw_input("Your username please? "))
print("Hello " + user.get("FirstName") + " " + user.get("LastName") + "!")
```

####PEA.users([<i>by</i>])

 - Returns a dict of all user profiles.

 - *by* specifies the type of key. *by* defaults to ```"Username"```

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

####PEA.classes([<i>by</i>])
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




Check out the examples at `PEA/examples` for more examples
###javascript module


##Goals:
 - Python API
	 - user data bindings
 - Javascript API
	 - user data bindings
	 - schedule/calendar bindings
	 - authentication bindings

##Todo:
 - Restructure
	 - Rename this repo PEA-connect-tools
	 - Or actually PEA-connect-python
	 - Make separate PEA.js repository
 - Make PEA-data-tools website on ECC
