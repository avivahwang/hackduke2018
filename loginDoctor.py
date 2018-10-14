import hashlib
from guizero import App, Text, TextBox, PushButton, Window
def finish():
	quit()
def allfilled():
	if (username.value != "" and password.value != "" and app.enabled):
		login.enable()
	else:
		login.disable()
FILENAME = "doctors.txt"
doctors = []
usernames = []
passhashes = []
try:
	with open(FILENAME) as d:
		for line in d:
			fields = line.split("\t")
			usernames.append(fields[1])
			passhashes.append(fields[2].strip())
except:
	err = App(title = "Error")
	message = Text(err, text = "There are no doctors in the database.\nPlease ask your doctor to register first.")
	badending = PushButton(err, text = "Exit", command = finish)
	err.display()
else:
	app = App(title = "Provider Login")
	greet = Text(app, text = "Welcome to litlitlit!\nThis is the login for providers.\n")
	prompt1 = Text(app, text = "Username:")
	username = TextBox(app, width = 20)
	prompt2 = Text(app, text = "Password:")
	password = TextBox(app, width = 20)
	success = Text(app, text = "")
	login = PushButton(app, text = "Login")
	login.disable()
	if app.enabled:
		success.repeat(100, allfilled)
	app.display()