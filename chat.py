'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket
from threading import *
import threading
from guizero import App, Text, TextBox, PushButton

print_lock = threading.Lock()
addresses = []

HOST = '127.0.0.1' #local host
PORT = 65432

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

def new_thread(conn, chat_num):
	def ending():
		app.destroy()
	def getinit():
		data = conn.recv(4096)
		if not data:
			print_lock.release()
			app.destroy()
		if data.decode('ascii') == 'exit':
			print_lock.release()
			prompt.value = 'Patient has ended the chat session.\nPlease close this window.'
			app.disable()
		history4.value = "Patient: %s" % (data.decode('ascii'))
		prompt.value = "What is your message?"
		goahead.enable()
	def push():
		def checknew():
			data = conn.recv(4096)
			history1.value = history2.value
			history2.value = history3.value
			history3.value = history4.value
			history4.value = "Patient: %s" % (data.decode('ascii'))
			if data.decode('ascii') == 'exit':
				print_lock.release()
				prompt.value = "Patient has ended the chat session.\nPlease close this window."
				app.disable()
		conn.send(message.value.encode('ascii'))
		if message.value == 'exit':
			app.destroy()
		history1.value = history2.value
		history2.value = history3.value
		history3.value = history4.value
		history4.value = "You: %s" % (message.value)
		message.clear()
		checknew()
	app = App(title = "Chat")
	nummessage = "Chat with patient number: %d" % (chat_num)
	chatnum = Text(app, text = nummessage)
	toptext = Text(app, text = 'Type "exit" at any time to leave this chat')
	history1 = Text(app, text = "")
	history2 = Text(app, text = "")
	history3 = Text(app, text = "")
	history4 = Text(app, text = "")
	prompt = Text(app, text = "Waiting for message...")
	message = TextBox(app, width = 25)
	goahead = PushButton(app, text = "Send", command = push)
	goahead.disable()
	app.after(10, getinit)
	app.display()
	conn.close()

def accept_connections():
	chat_number = 1
	while True:
		conn, addr = s.accept()
		#print('Starting chat with patient number:',chat_number)
		addresses.append(addr)
		print_lock.acquire()
		#start_new_thread(new_thread,(s,conn,chat_number))
		Thread(target=new_thread, args=(conn,chat_number)).start()
		chat_number += 1


def Main():
	#s.bind((socket.gethostname(), PORT))
	s.listen(5)
	accept = Thread(target=accept_connections)
	accept.start()
	accept.join()
	s.close()

if __name__ == '__main__':
	Main()
