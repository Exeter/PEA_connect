#PEA-data-tools
<br>
<br>
Tools for working with PEA data!
<br>
<br>
<br>

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

input = raw_input("Username: ")
user = users.byUsername(input)

output = "Hello, " + user.get("FirstName") + " " + user.get("LastName")
print(output)

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
 - change "update" methods in connect.py to get json from ecc.exeter.edu. Create "download" methods for actual scraping straight from the connect.exeter.edu
 - write python documentation
 - write browser/node javascript module for working with user data (note: create a git subfolder)
 - Communicate with IT about this
