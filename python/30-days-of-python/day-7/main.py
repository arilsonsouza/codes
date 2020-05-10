msg_template = """Hello {name},
Thank you for joining {website}. We are very
happy to have you with us.
"""

def format_mg(name="Arilson", website="aos.sh"):
	msg = msg_template.format(name=name, website=website)
	return msg


"""
"{} {}".format("abc", 123)
"{1} {2}".format("abc", 123)
"{name} {number}".format(name="abc", number=123)
"{} {name} {number}".format("abc",name="abc", number=123)
"""