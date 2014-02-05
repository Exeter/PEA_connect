from PEA_connect import data
#A behind the scenes generation of detaileduserdata.json
#Not an example per se, but more like a debugging test


def test_getRawUserData():
	#a = data.getRawUserData()
	b = data.getRawUserData()
	assert b
def test_getBasicUserData():
	#a = data.getBasicUserData()
	b = data.getBasicUserData()
	assert b

def test_getDetailedUserData():
	b = data.getDetailedUserData()
	assert b

def test_getClassData():
	b = data.getClassData()
	assert b
if __name__ == '__main__':
	test_getRawUserData()
	test_getBasicUserData()
	test_getDetailedUserData()
	test_getClassData()
