#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date    : 2018-07-15 00:56:20
# @Author  : Simon (simon.xie@codewalker.meg)
# @Link    : http://www.codewalker.me
# @Version : 1.0.0

import socket

def main():
#     host = "127.0.0.1"
#     port = 5000

    address = ("127.0.0.1", 5000)
    mySocket = socket.socket()
    mySocket.bind(address)
     
    mySocket.listen(3)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))
             
            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())
             
    conn.close()
if __name__ == "__main__":
    main()

