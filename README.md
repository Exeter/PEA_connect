#PEA_connect
PEA_connect is a python module that facilitates the retrieval of Exeter Connect user data.

All of the information gathered by PEA-data-tools can be found on official Academy websites under ordinary usage methods.

##Easy?
Here's a basic example:
```python
import PEA_connect

users = PEA_connect.users()	#downloads data, or loads from a cache

user = users.get(raw_input("Your username please: "))	#asks for your username
print("Hello " + user.get("FirstName") + " " + user.get("LastName") + "!")	#prints your name
print("You live in " + user.get("PEALivingGroup") + ".")	#prints your dorm
print("Your PO Box number is " + user.get("POBox") + ".")	#prints your PO number
```

[More examples](PEA_/examples/README.md)

##Installation
Supports python 2 only.

Requires [suds](https://fedorahosted.org/suds/). Install it with:
```
pip install suds
```
_TODO_ write/design installation of actual module

##Methods

####PEA_connect.users( [ <i>by</i> ] )

 - Returns a dict of all user profiles.

 - *by* specifies the type of key. Given no arguments, *by* defaults to ```"Username"```

 - Valid key types: ```"Username"```, ```"EmployeeID"```, ```"UserProfile_GUID"```
 - Example usage:
	```python
	import PEA_connect

	byUsername = PEA_connect.users()	#same as PEA_connect.users(by="Username")
	byID = PEA_connect.users(by="EmployeeID")

	a = byUsername.get('slee2')
	b = byID.get('0704298')
	assert a == b	#True, because slee2's ID is 0704298
	```

####PEA_connect.classes( [ <i>by</i> ] )
 - Returns a dict of all class profiles.

 - *by* specifies the type of key. *by* defaults to ```"FullString"```

 - Valid key types: ```"FullString"```, ```"ClassCode"```, ``"ClassID"```
 - Example usage:
	```python
	import PEA_connect

	byFullString = PEA_connect.classes()	#same ass PEA_connect.classes(by="FullString")
	byClassCode = PEA_connect.classes(by="ClassCode")
	
	a = byFullString.get("13/FA Selected Topics * (MAT-590-A)#/classes/mat-590-a-cs81877")
	b = byClassCode.get("mat-590-a")
	assert a == b	#True
	```
##Todo:
 - Add to README how an actual user/class data looks like in JSON
 - Make PEA-data-tools website on ECC
 - Make changes to code that reflect README
  - simplify to single file, get rid of unnecessary package structure
