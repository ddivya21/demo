#!usr/bin/python

import  socket
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True :
	msg=raw_input("enter your msg")
	x.sendto(msg,("",5555))
	print x.recvfrom(100)

