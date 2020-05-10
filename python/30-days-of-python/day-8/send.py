import sys
import requests
from datetime import datetime
from formatting import format_msg

def send(name, website=None, verbose=False):

	if website != None:
		msg = format_msg(name=name, website=website)
	else:
		msg = format_msg(name=name)
	if verbose:
		print(name, website)
	r = requests.get('http://httpbin.org/json')
	if r.status_code == 200:
		return r.json()
	else:
		return "There was an error"


if __name__ == "__main__":	
	name = "Unknow"
	if len(sys.argv) > 1:
		name = sys.argv[1]
	resp = send(name, verbose=True)
	print(resp)