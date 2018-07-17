#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 12:55:35
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import socket
 
def Main():
        host = '127.0.0.1'
        port = 5000
         
        mySocket = socket.socket()
        mySocket.connect((host,port))
         
        message = input(" -> ")
         
        while message != 'q':
                mySocket.send(message.encode())
                data = mySocket.recv(1024).decode()
                 
                print ('Received from server: ' + data)
                 
                message = input(" -> ")
                 
        mySocket.close()
 
if __name__ == '__main__':
    Main()

    print('xxxx')

