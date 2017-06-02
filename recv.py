#!/usr/bin/python
import socket

x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
x.bind(("",5555))

while True:
	data=x.recvfrom(100)
	print "msg from client :",data[0]
	print"--------------------------"
	print "client address :",data[1][0]
	print"--------------------------"
	r=raw_input("type your rply")
	x.sendto(r,data[1])
