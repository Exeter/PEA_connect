from PEA import data
import json

def confirm(prompt):
	ans = raw_input(prompt)
	valid = ['Y']
	if not ans in valid:
		exit()
def updateAll():
	print(':: updating raw collection of users...')
	data.updateRawUserCollection()
	print(':: updating basic info...')
	data.updateBasicInfo()
	print(':: updating detailed info...')
	#data.updateDetailedInfo()
	print(':: update complete!')

if __name__ == '__main__':
	confirm(':: Proceed with data update? [Y/n] ')
	updateAll()
