import sys
import hashlib
import os
from guizero import App, Text, TextBox, PushButton
def finish():
	quit()
def adduser():
	passhashed = hashlib.sha256(password.value.encode()).hexdigest()
	if not usernames:
		towrite = "%s\t%s" % (username.value,passhashed)
	else:
		towrite = "\n%s\t%s" % (username.value,passhashed)
	with open(FILENAME, "a") as d:
		d.write(towrite)
		exit.enable()
		exit.show()
def checkgood():
	if username.value in usernames:
		success.value = "This username is already taken. Please try another."
	else:
		success.value = "Registration successful!"
		app.disable()
		adduser()
def allfilled():
	if (username.value != "" and password.value != "" and app.enabled):
		confirm.enable()
	else:
		confirm.disable()
FILENAME = "patients.txt"
patients = []
usernames = []
passhashes = []
try:
	with open(FILENAME) as d:
		for line in d:
			fields = line.split("\t")
			usernames.append(fields[0])
			passhashes.append(fields[1].strip())
except:
	d = open(FILENAME,"w+")
	d.close()
app = App(title = "New user registration")
intro = Text(app, text = "Welcome to Litlitlit!\n")
prompt2 = Text(app, text = "Please enter your username.")
username = TextBox(app, width = 20)
prompt3 = Text(app, text = "Please enter your password.")
password = TextBox(app, width = 20)
password.tk.config(show="*")
txt2 = Text(app, text = "")
confirm = PushButton(app, text = "Confirm registration", command = checkgood)
confirm.disable()
success = Text(app, text = "")
exit = PushButton(app, text = "Finish", command = finish)
exit.hide()
if app.enabled:
	success.repeat(100, allfilled)
app.display()