import sys
import requests
from datetime import datetime
from formatting import format_msg
from send_mail import send_mail

def send(name, website=None, to_email=None, verbose=False):
	assert to_email != None

	if website != None:
		msg = format_msg(name=name, website=website)
	else:
		msg = format_msg(name=name)
	if verbose:
		print(name, website, to_email)
	
	# send the message
	try:
		send_mail(text=msg, to_emails=[to_email], html=None)
		sent = True
	except:
		sent = False
	
	return sent
if __name__ == "__main__":	
	name = "Unknow"
	if len(sys.argv) > 1:
		name = sys.argv[1]
		email = None
		if len(sys.argv) > 2:
			email = sys.argv[2]
	resp = send(name, to_email=email, verbose=True)
	print(resp)