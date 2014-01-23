from PEA import data
def test_getRawUserData():
	#a = data.getRawUserData()
	b = data.getRawUserData(source="connect")
	assert b
def test_getBasicUserData():
	#a = data.getBasicUserData()
	b = data.getBasicUserData(source='connect')
	assert b

def test_getDetailedUserData():
	b = data.getDetailedUserData(source='connect', cache="True")
	assert b

def test_getClassData():
	b = data.getClassData(source='generate', cache="True")
	assert b
if __name__ == '__main__':
	test_getRawUserData()
	test_getBasicUserData()
	test_getDetailedUserData()
	test_getClassData()
