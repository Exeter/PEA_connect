from PEA import connect
from getpass import getpass
import sys
import re
import string
import json

#Everything concerned about data generation/retrieval


#TODO: clean
uname = ""
pword = ""

rawuserdata_path = './data/raw_user_data.json'
def _authenticate():
	global uname, pword
	if not uname:
		print(':: Authentication required to connect to Exeter Connect')
		uname = raw_input('Username: ') + '@exeter.edu'
		pword = getpass()
		
def updateRawUserData():
	_authenticate()

	UserGroup = connect.getclient('https://connect.exeter.edu/_vti_bin/usergroup.asmx?WSDL', uname, pword)
	output = json.dumps(connect.to_dict(UserGroup.service.GetAllUserCollectionFromWeb()), indent=4, sort_keys=True)

	f = open(rawuserdata_path, 'w')
	f.write(output)
	f.close()
def getRawUserData():
	f = open(rawuserdata_path, 'r')
	return json.loads(f.read())

# Basic info
basicuserdata_path = './data/basic_user_data.json'
notpeople = ['spsearchservice', 'spsearchcontent', 'spsetup', 'spcachesuper', 'spreader']
def updateBasicUserData():
	raw = getRawUserData()
	output = {}
	for user in raw['GetAllUserCollectionFromWeb']['Users']['User']:
		u = {}
		u['login'] = user['_LoginName']
		u['internal_id'] = user['_ID']
		u['email'] = user['_Email']
		u['name'] = user['_Name']

		if not (user['_LoginName'].startswith("i:0#.w|master\\")):
			continue #filter out non-people

		username = user['_LoginName'][14:]
		if username in notpeople:
			continue #filter out non-people

		u['username'] = username

		output[username] = u
	g = open(basicuserdata_path, 'w')
	g.write(json.dumps(output, indent=4, sort_keys=True))
	g.close()
def getBasicUserData():
	f = open(basicuserdata_path, 'r')
	return json.loads(f.read())

# Detailed info
detaileduserdata_path = './data/detailed_user_data.json'
def updateDetailedUserData():
	_authenticate()

	UserProfileService = connect.getclient('https://connect.exeter.edu/student/_vti_bin/UserProfileService.asmx?WSDL', uname, pword)
	def getProfile(user):
		def cleandict(dirty):
			output = {}
			for x in dirty['PropertyData']:
				if x['Privacy'] == "Private":
					continue
				k = x['Name']
				if k == 'employeeID':
					k = 'EmployeeID'
				elif k == 'UserName':
					k = 'Username'
				elif k == 'Courses':
					k = 'Classes'

				values = x['Values']
				if values =="":
					continue
				v = []
				for value in values['ValueData']:
					v.append(value['Value'])
				if (len(v) == 1) and (k not in ['Organizations', 'Classes']):
					v = v[0]
				output[k] = v
			return output
		raw = connect.to_dict(UserProfileService.service.GetUserProfileByName(user['login']))
		return cleandict(raw)

	basicinfo = getBasicInfo()
	output = {}
	counter = 0
	for user in basicinfo:
		try:
			output[user] = getProfile(basicinfo[user])
			print(str(counter) + " out of " +  str(len(basicinfo)) +  " | " + user)
		except:
			pass
		counter += 1
	
	g = open(detaileduserdata_path, 'w')
	g.write(json.dumps(output, indent=4, sort_keys=True))
	g.close()
def getDetailedUserData():
	f = open(detaileduserdata_path, 'r')
	return json.loads(f.read())

# Classes
classdata_path = './data/classdata.json'
def updateClassData():
	people = getDetailedUserData()
	students = dict((k, v) for k, v in people.items() if 'SourceCode' in v.keys() and "ST" in v['SourceCode'].split(','))
	teachers = dict((k, v) for k, v in people.items() if 'SourceCode' in v.keys() and "F" in v['SourceCode'].split(','))

	classes = {}
	for name, student in students.items():
		if 'Classes' in student.keys():
			for c in student['Classes']:
				if c not in classes.keys():
					info = c[c.rfind('/') + 1:].split('-')

					classes[c] = {'Students': [], 'Teacher': None}

					classes[c]['FullString'] = c;
					classes[c]['Name'] = c[c.index(' ') + 1:re.search(r'[*(]',c).start()].strip()
					classes[c]['ClassCode'] = '-'.join(info[:-1])
					classes[c]['SubjectCode'] = info[0]
					classes[c]['CourseNumber'] = info[1]
					classes[c]['Formats'] = list(filter(lambda x: x in string.ascii_letters, info[2]))
					classes[c]['ClassID'] = info[len(info) - 1][2:]
				classes[c]['Students'].append(name)
	#Adds teachers to classes
	for name, teacher in teachers.items():
		if 'Classes' in teacher.keys():
			for c in teacher['Classes']:
				try:
					classes[c]['Teacher'] = name
				except KeyError:
					pass

	g = open(classdata_path, 'w')
	g.write(json.dumps(classes, indent=4, sort_keys=True))
	g.close()
def getClassData():
	f = open(classdata_path, 'r')
	return json.loads(f.read())

