'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket
from _thread import *
import threading

print_lock = threading.Lock()

def new_thread(conn):
    while True:
        data = conn.recv(4096)
        if not data:
            print_lock.release()
            break
        print('Received message from patient:', data.decode('ascii'))
        doc_message = input("Doctor, what is your message? ")
        conn.send(doc_message.encode('ascii'))
    conn.close()

def Main():
    HOST = '127.0.0.1' #local host
    PORT = 65432
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST,PORT))
    #s.bind((socket.gethostname(), PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print_lock.acquire()
        #print('Connected by', addr)
        start_new_thread(new_thread,(conn,))
        
if __name__ == '__main__':
    Main()