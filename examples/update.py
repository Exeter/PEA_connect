from .. import data
import json
#updates local copies of data

def confirm(prompt):
	ans = raw_input(prompt)
	valid = ['Y']
	if not ans in valid:
		exit()
def updateAll():
	print(':: updating user data...')
	data.getDetailedUserData(from_cache=False, to_cache=True)
	print(':: generating class data...')
	data.getClassData(from_cache=False, to_cache=True)
	print(':: update complete!')

if __name__ == '__main__':
	confirm(':: Proceed with data update? [Y] ')
	updateAll()
