#PEA-data-tools
<br>
<br>
Tools for working with PEA data!
<br>
<br>
<br>
####These tools are still in alpha stage! Names/bindings are bound to change. Use at your own risk/(in)convenience!

##Info:
The purpose of these tools is to make PEA data more accessible for student developers; to facilitate students in creating applications useful and relevant to the PEA community.

These tools organize and make public data more accessible for student developers; all of the information gathered by PEA-data-tools can be found on official Academy websites under ordinary usage.

##Currently implemented:
###python module
Currently facillitates retrieval of Exeter Connect user data. 
Requires [suds](https://fedorahosted.org/suds/)


Basic Example:
```python
from PEA import users

user = users().get("slee2")

print("Hello, " + user.get("FirstName") + " " + user.get("LastName"))

```



Check out the examples at `PEA/examples` for more examples
###javascript module


#Goals:
 - api for python
 - api for javascript
 - user data bindings
 - schedule/calendar bindings
 - authentication bindings

#TODO
 - Rename courses in data.jsons to classes
 - Write tests
	 - Test update example
 - Simplify API
	 - Phase out raw_user_info.json and basic_user_info.json
 - make basicinfo keys CamelCase
 - change "update" methods in connect.py to get json from ecc.exeter.edu. Create "download" methods for actual scraping straight from the connect.exeter.edu
 - write python documentation
 - Communicate with IT about this
