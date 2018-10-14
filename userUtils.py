import hashlib
from guizero import App, Text, TextBox, PushButton, Window
def signupDoctor():
	def finish():
		app.destroy()
	def adduser():
		passhashed = hashlib.sha256(password.value.encode()).hexdigest()
		ret.append(name.value)
		ret.append(username.value)
		ret.append(passhashed)
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
		if (name.value != "" and username.value != "" and password.value != "" and app.enabled):
			confirm.enable()
		else:
			confirm.disable()
	FILENAME = "doctors.txt"
	doctors = []
	usernames = []
	passhashes = []
	ret = []
	try:
		with open(FILENAME) as d:
			for line in d:
				fields = line.split("\t")
				doctors.append(fields[0])
				usernames.append(fields[1])
				passhashes.append(fields[2].strip())
	except:
		d = open(FILENAME,"w+")
		d.close()
	app = App(title = "New doctor registration")
	intro = Text(app, text = "Welcome to AnonyComm!\n")
	prompt1 = Text(app, text = "Please enter your name (First Last).")
	name = TextBox(app, width = 20)
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
	return ret
def signupPatient():
	def finish():
		app.destroy()
	def finish2():
		quit()
	def writedata():
		ind = docnames.index(docname.value)
		docHashed = hashlib.sha256(docusernames[ind].encode()).hexdigest()
		passhashed = hashlib.sha256(password.value.encode()).hexdigest()
		ret.append(username.value)
		ret.append(docHashed)
		ret.append(passhashed)
		findmatch.destroy()
		exit.enable()
		exit.show()
	def matchDoctor():
		if docname.value in docnames:
			earlyexit.hide()
			findmatch.disable()
			writedata()
		else:
			matchintro.value = "Your doctor's name cannot be found.\n(S)he may not have created an account yet."
			earlyexit.show()
	def checkgood():
		if username.value in usernames:
			success.value = "This username is already taken. Please try another."
		else:
			success.value = "Registration successful!"
			app.disable()
			findmatch.enable()
			findmatch.show()
	def allfilled():
		if (username.value != "" and password.value != "" and app.enabled):
			confirm.enable()
		else:
			confirm.disable()
	FILENAME = "patients.txt" # Format: username TAB hashedDocUsername TAB hashedPassword
	DOCTORS = "doctors.txt" # Format: name TAB username TAB hashedPassword
	patients = []
	usernames = []
	docnames = []
	docusernames = []
	ret = []
	try:
		with open(FILENAME) as p:
			for line in p:
				fields = line.split("\t")
				usernames.append(fields[0])
	except:
		p = open(FILENAME,"w+")
		p.close()
	try:
		with open(DOCTORS) as d:
			for line in d:
				fields = line.split("\t")
				docnames.append(fields[0])
				docusernames.append(fields[1])
	except:
		err = App(title = "Error")
		message = Text(err, text = "There are no doctors in the database.\nPlease ask your doctor to register first.")
		badending = PushButton(err, text = "Exit", command = finish2)
		err.display()
	else:
		app = App(title = "New patient registration")
		intro = Text(app, text = "Welcome to AnonyComm!\n")
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
		findmatch = Window(app,title = "Doctor name entry")
		matchintro = Text(findmatch,"Please enter your doctor's name (First Last)")
		docname = TextBox(findmatch, width = 20)
		checkdoc = PushButton(findmatch, text = "Find your doctor", command = matchDoctor)
		earlyexit = PushButton(findmatch, text = "Quit", command = finish)
		earlyexit.hide()
		findmatch.hide()
		if app.enabled:
			success.repeat(100, allfilled)
		app.display()
		return ret
def loginDoctor():
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
			ret.append(username.value)
			ret.append(True)
		app.destroy()
	FILENAME = "doctors.txt"
	usernames = []
	passhashes = []
	ret = []
	try:
		with open(FILENAME) as d:
			for line in d:
				fields = line.split("\t")
				usernames.append(fields[1])
				passhashes.append(fields[2].strip())
	except:
		err = App(title = "Error")
		message = Text(err, text = "There are no doctors in the database.\nPlease register first.")
		badending = PushButton(err, text = "Exit", command = finish)
		err.display()
		return["",False]
	else:
		app = App(title = "Provider Login")
		greet = Text(app, text = "Welcome to AnonyComm!\nThis is the login for providers.\n")
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
			ret = ["",False]
		return ret
def loginPatient():
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
		greet = Text(app, text = "Welcome to AnonyComm!\nThis is the login for patients.\n")
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