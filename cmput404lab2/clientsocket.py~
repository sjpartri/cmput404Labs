#!/user/bin/env python

# Copyright (c) Sean Partridge

import socket

#AF_INET want a socket on the iternet
#SOCK_STREAM = TCP
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

clientSocket.connect(("www.google.com",80))

request = "GET /HTTP/1.0\n\n"

clientSocket.sendall(request)

response = bytearray()

while True:
	part = clientSocket.recv(1024)
	if (part):
		response.extend(part)
	else:
		break 

print response 
