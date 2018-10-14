'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket
from threading import *
import threading
from guizero import App, Text, TextBox, PushButton

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def execute_client():
	def push():
		def checknew():
			data = s.recv(4096)
			history1.value = history2.value
			history2.value = history3.value
			history3.value = history4.value
			history4.value = "Doctor: %s" % (data.decode('ascii'))
			if data.decode('ascii') == 'exit':
				prompt.text = "Doctor has ended the chat session"
				app.disable()
		s.send(message.value.encode('ascii'))
		if message.value == 'exit':
			app.destroy()
		history1.value = history2.value
		history2.value = history3.value
		history3.value = history4.value
		history4.value = "You: %s" % (message.value)
		message.clear()
		checknew()
	app = App(title = "Chat")
	toptext = Text(app, text = 'Type "exit" at any time to leave this chat\n')
	history1 = Text(app, text = "")
	history2 = Text(app, text = "")
	history3 = Text(app, text = "")
	history4 = Text(app, text = "")
	prompt = Text(app, text = "What is your message?")
	message = TextBox(app, width = 25)
	goahead = PushButton(app, text = "Send", command = push)
	app.display()
	s.close()

def Main():
	s.connect((HOST,PORT))
	this_thread = Thread(target=execute_client)
	this_thread.start()

if __name__ == '__main__':
	Main()
