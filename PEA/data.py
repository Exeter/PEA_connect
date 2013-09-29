from PEA import connect
import sys
import re
import string
import json

#Everything concerned about data generation/retrieval
#ideal getBlahBlah(source="cache", cache=False )

def _confirm(prompt):
	ans = raw_input(prompt)
	valid = ['Y']
	if not ans in valid:
		exit()

def _getDataGenerator(path, sources):
	def getData(source="cache", cache=False):
		output = {}
		if source == "cache":
			try:
				f = open(path,'r')
				output = json.loads(f.read())
			except:
				raise Exception(path + " does not exist")
		else:
			output = sources[source]()
			if cache:
				print(":: Caching " + path)
				tocache = json.dumps(output, indent=4, sort_keys=True)

				f = open(path, 'w+')
				f.write(tocache)
				f.close()
		return output
	return getData

# Raw User Data
def _getRawUserData():
	path = './data/raw_user_data.json'
	sources = {}
	def fromconnect():
		print(":: Downloading raw user data")
		UserGroup = connect.getclient('https://connect.exeter.edu/_vti_bin/usergroup.asmx?WSDL')
		return connect.to_dict(UserGroup.service.GetAllUserCollectionFromWeb())
	sources['connect'] = fromconnect
	return _getDataGenerator(path, sources)
getRawUserData = _getRawUserData()

# Basic User Data
def _getBasicUserData():
	path = './data/basic_user_data.json'
	sources = {}
	def fromconnect():
		print(":: Generating data basic user data")
		raw = getRawUserData(source="connect")

		output = {}
		notpeople = ['spsearchservice', 'spsearchcontent', 'spsetup', 'spcachesuper', 'spreader']
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
		return output
	sources['connect'] = fromconnect
	return _getDataGenerator(path, sources)
getBasicUserData = _getBasicUserData()

	
# Detailed User Data
def _getDetailedUserData():
	path = './data/detailed_user_data.json'
	sources = {}
	def fromconnect():
		basicinfo = getBasicUserData(source="connect")
		output = {}

		print(":: Downloading detailed user data...")
		UserProfileService = connect.getclient('https://connect.exeter.edu/student/_vti_bin/UserProfileService.asmx?WSDL')

		def getProfile(user):
			def clean(dirtyprofile):
				output = {}
				for x in dirtyprofile['PropertyData']:
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
			dirtyprofile = connect.to_dict(UserProfileService.service.GetUserProfileByName(user['login']))
			return clean(dirtyprofile)

		counter = 0
		for username in basicinfo:
			try:
				print(":: Downloading profile of " + username + "\t\t\t|\t" + str(counter) + " out of " +  str(len(basicinfo)))
				output[username] = getProfile(basicinfo[username])
			except:
				print(":: FAILED!")
				pass
			counter += 1
		return output
	sources['connect'] = fromconnect
	return _getDataGenerator(path, sources)
getDetailedUserData = _getDetailedUserData()

# Class Data
def _getClassData():
	path = './data/class_data.json'
	sources = {}
	def generate():
		people = getDetailedUserData()
		filterByCode = lambda s: dict((k, v) for k, v in people.items() if 'SourceCode' in v.keys() and s in v['SourceCode'].split(','))
		students = filterByCode("ST")
		teachers = filterByCode("F")

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

		g = open(path, 'w+')
		g.write(json.dumps(classes, indent=4, sort_keys=True))
		g.close()
		return classes
	sources['generate'] = generate
	return _getDataGenerator(path, sources)
getClassData = _getClassData()
