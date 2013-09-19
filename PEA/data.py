from . import connect
from getpass import getpass
import sys
import json


uname = ""
pword = ""

usercollection_path = './data/raw/user_collection.json'
def _authenticate():
	global uname, pword
	if not uname:
		print(':: Authentication required to connect to Exeter Connect')
		uname = raw_input('Username: ') + '@exeter.edu'
		pword = getpass()
		
def updateRawUserCollection():
	_authenticate()

	UserGroup = connect.getclient('https://connect.exeter.edu/_vti_bin/usergroup.asmx?WSDL', uname, pword)
	output = json.dumps(connect.to_dict(UserGroup.service.GetAllUserCollectionFromWeb()), indent=4, sort_keys=True)

	f = open(usercollection_path, 'w')
	f.write(output)
	f.close()
def getRawUserCollection():
	f = open(usercollection_path,'r')
	return json.loads(f.read())

# Basic info
basicinfo_path = './data/basicinfo.json'
notpeople = ['spsearchservice', 'spsearchcontent', 'spsetup', 'spcachesuper', 'spreader']
def updateBasicInfo():
	raw = getRawUserCollection()
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
	g = open(basicinfo_path, 'w')
	g.write(json.dumps(output, indent=4, sort_keys=True))
	g.close()
def getBasicInfo():
	f = open(basicinfo_path, 'r')
	return json.loads(f.read())

# Detailed info
detailedinfo_path = './data/detailedinfo.json'
def updateDetailedInfo():
	_authenticate()

	UserProfileService = connect.getclient('https://connect.exeter.edu/student/_vti_bin/UserProfileService.asmx?WSDL', uname, pword)
	def getProfile(user):
		def cleandict(dirty):
			output = {}
			for x in dirty['PropertyData']:
				if x['Privacy'] == "Private":
					continue
				k = x['Name']

				values = x['Values']
				if values =="":
					continue
				v = []
				for value in values['ValueData']:
					v.append(value['Value'])
				if (len(v) == 1) and (k not in ['Organizations', 'Courses']):
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
	
	g = open(detailedinfo_path, 'w')
	g.write(json.dumps(output, indent=4, sort_keys=True))
	g.close()
def getDetailedInfo():
	f = open(detailedinfo_path, 'r')
	return json.loads(f.read())
