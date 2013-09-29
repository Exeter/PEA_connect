#!/usr/bin/env python2

from suds.client import Client
from suds.transport.https import HttpAuthenticated
from suds.sudsobject import asdict
from getpass import getpass
import json

uname = ""
pword = ""
def _authenticate():
	global uname, pword
	if not uname:
		print(':: Authentication required to access Exeter Connect:')
		uname = raw_input('Username: ') + '@exeter.edu'
		pword = getpass()


def getclient(url):
	print(':: Connecting to ' + url)
	_authenticate()
	credentials = dict(username = uname, password=pword)
	t = HttpAuthenticated(**credentials);
	return Client(url, transport=t)

def to_dict(sudsobject):
	d = sudsobject
	out = {}
	for k, v in asdict(d).iteritems():
		if hasattr(v, '__keylist__'):
			out[k] = to_dict(v)
		elif isinstance(v, list):
			out[k] = []
			for item in v:
				if hasattr(item, '__keylist__'):
					out[k].append(to_dict(item))
				else:
					out[k].append(item)
		else:
			out[k] = v
	return out
