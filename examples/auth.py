from PEA import auth
from getpass import getpass

print(":: Authentication example ::")

uname = raw_input('Username: ')
pword = getpass()

print(auth(uname, pword))
