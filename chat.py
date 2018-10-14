'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket
from _thread import *
from threading import *
import threading

print_lock = threading.Lock()
addresses = []

HOST = '127.0.0.1' #local host
PORT = 65432
    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))

def new_thread(conn, chat_num):
    print('Type "exit" at any time to leave this chat')
    while True:
        data = conn.recv(4096)
        if not data:
            print_lock.release()
            break
        if data.decode('ascii') == 'exit':
            print_lock.release()
            print('Patient has ended the chat session')
            break
        print 'Received message from patient:', data.decode('ascii')
        doc_message = input("Doctor, what is your message? ")
        conn.send(doc_message.encode('ascii'))
        if doc_message == 'exit':
            break
    print 'Now closing chat with patient', chat_num
    conn.close()
    
def accept_connections():
    chat_number = 1
    while True:
        conn, addr = s.accept()
        print('Starting chat with patient number:',chat_number)
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