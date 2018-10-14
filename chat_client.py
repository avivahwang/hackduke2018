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
        message = raw_input("What is your message? ")
        s.send(message.encode('ascii'))
        if message == 'exit':
            break
        data = s.recv(4096)
        if data.decode('ascii') == 'exit':
            print 'Doctor has ended the chat session'
            break
        print 'Received message from doctor:', data.decode('ascii')
    s.close()
    
def Main():
    s.connect((HOST,PORT))
    this_thread = Thread(target=execute_client)
    this_thread.start()
    
if __name__ == '__main__':
    Main()