order=raw_input("""
*****************
Joe's Snack House
*****************
Choose one:
a) I'd like a snack.
b) I'd like some spam.
c) I'd like the check.
Prompt:>""")

if order == "a":
	print "Here's a snack!"
elif order == "b":
	print "Here's some spam!"
elif order == "c":
	print "Here's the check!"
else:
	print "I'm afraid you get nothing!"
