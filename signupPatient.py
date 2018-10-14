import hashlib
from guizero import App, Text, TextBox, PushButton, Window

def main():
	def finish():
		app.destroy()


	def writedata():
		ind = docnames.index(docname.value)
		docHashed = hashlib.sha256(docusernames[ind].encode()).hexdigest()
		passhashed = hashlib.sha256(password.value.encode()).hexdigest()
		ret.append(username.value)
		ret.append(docHashed)
		ret.append(passhashed)
		if not usernames:
			towrite = "%s\t%s\t%s" % (username.value,docHashed,passhashed)
		else:
			towrite = "\n%s\t%s\t%s" % (username.value,docHashed,passhashed)
		with open(FILENAME, "a") as p:
			p.write(towrite)
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
		badending = PushButton(err, text = "Exit", command = finish)
		err.display()
	else:
		app = App(title = "New patient registration")
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

if __name__ == "__main__":
	main()
