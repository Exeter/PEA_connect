from PEA_connect import users
import json

def pprint(x):
	print(json.dumps(x, indent=4, sort_keys=True))

data = users()
def query():
	target = str(raw_input('username: '))
	output = data.get(target)
	if not output:
		print("user not found")
		return
	pprint(output)
if __name__ == "__main__":
	while True:
		query()
