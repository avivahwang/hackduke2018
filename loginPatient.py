import hashlib
from guizero import App, Text, TextBox, PushButton, Window
def Main():
	def finish():
		err.destroy()
	def allfilled():
		if (username.value != "" and password.value != "" and app.enabled):
			login.enable()
		else:
			login.disable()
	def verify():
		passhashed = hashlib.sha256(password.value.encode()).hexdigest()
		if username.value in usernames:
			ind = usernames.index(username.value)
			if passhashed == passhashes[ind]:
				success.value = "Logged in"
				app.disable()
				cont.enable()
				cont.show()
			else:
				success.value = "Incorrect password"
		else:
			success.value = "Username not found"
	def endfunc():
		if cont.enabled:
			ind = usernames.index(username.value)
			ret.append(username.value)
			ret.append(dochashes[ind])
			ret.append(True)
		app.destroy()
	FILENAME = "patients.txt"
	dochashes = []
	usernames = []
	passhashes = []
	ret = []
	try:
		with open(FILENAME) as d:
			for line in d:
				fields = line.split("\t")
				usernames.append(fields[0])
				dochashes.append(fields[1])
				passhashes.append(fields[2].strip())
	except:
		err = App(title = "Error")
		message = Text(err, text = "There are no patients in the database.\nPlease register first.")
		badending = PushButton(err, text = "Exit", command = finish)
		err.display()
		return["","",False]
	else:
		app = App(title = "Patient Login")
		greet = Text(app, text = "Welcome to litlitlit!\nThis is the login for patients.\n")
		prompt1 = Text(app, text = "Username:")
		username = TextBox(app, width = 20)
		prompt2 = Text(app, text = "Password:")
		password = TextBox(app, width = 20)
		password.tk.config(show="*")
		login = PushButton(app, text = "Login", command = verify)
		login.disable()
		success = Text(app, text = "")
		cont = PushButton(app, text = "Continue", command = endfunc)
		cont.hide()
		if app.enabled:
			success.repeat(100, allfilled)
		app.on_close(endfunc)
		app.display()
		if not ret:
			ret = ["","",False]
		return ret
if __name__ == "__main__":
	Main()