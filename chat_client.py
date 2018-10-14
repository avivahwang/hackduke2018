'''
Created on Oct 13, 2018

@author: avivahwang
'''

import socket

def Main():
    HOST = '127.0.0.1'
    PORT = 65432
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST,PORT))
    while True:
        message = input("What is your message? ")
        s.send(message.encode('ascii'))
        data = s.recv(4096)
        print('Received message from doctor:', data.decode('ascii'))
        ask = input("Do you want to exit this chat? (y/n) ")
        if ask == 'y':
            break
        else:
            continue
    s.close()
    
if __name__ == '__main__':
    Main()