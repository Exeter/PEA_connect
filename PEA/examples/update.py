from .. import data
import json
#updates local copies of data
#TODO: update to new data.py api

def confirm(prompt):
	ans = raw_input(prompt)
	valid = ['Y']
	if not ans in valid:
		exit()
def updateAll():
	print(':: updating user data...')
	data.getDetailedUserData(source='connect')
	print(':: generating class data...')
	data.getClassData(source="generate", cache=True)

	print(':: update complete!')

if __name__ == '__main__':
	confirm(':: Proceed with data update? [Y/n] ')
	updateAll()
