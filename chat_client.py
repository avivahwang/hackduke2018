'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket
from _thread import *
from threading import *
import threading

HOST = '127.0.0.1'
PORT = 65432
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
def execute_client():
    print 'Type "exit" at any time to leave this chat'

    while True:
        message = input("What is your message? ")
        s.send(message.encode('ascii'))
        if message == 'exit':
            break
        data = s.recv(4096)
<<<<<<< HEAD
        if data.decode('ascii') == 'exit':
            print 'Doctor has ended the chat session'
=======
        print('Received message from doctor:', data.decode('ascii'))
        ask = input("Do you want to exit this chat? (y/n) ")
        if ask == 'y':
>>>>>>> f8d026c6fc6983a9eeba79f28a39d66a7f2f19ce
            break
        print 'Received message from doctor:', data.decode('ascii')
    s.close()
    
def Main():
    s.connect((HOST,PORT))
    this_thread = Thread(target=execute_client)
    this_thread.start()
    
if __name__ == '__main__':
    Main()