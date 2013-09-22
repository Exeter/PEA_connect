from .. import data
import json
#updates local copies of data

def confirm(prompt):
	ans = raw_input(prompt)
	valid = ['Y']
	if not ans in valid:
		exit()
def updateAll():
	print(':: updating raw user data...')
	data.updateRawUserData()
	print(':: updating basic user data...')
	data.updateBasicUserData()
	print(':: updating detailed user data...')
	data.updateDetailedUserData()
	print(':: updating class data...')
	data.updateClassData()

	print(':: update complete!')

if __name__ == '__main__':
	confirm(':: Proceed with data update? [Y/n] ')
	updateAll()
