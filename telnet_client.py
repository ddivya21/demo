#!/usr/bin/python

import socket,os,commands,time,sys
x=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

user=raw_input("enter user name :")
password=raw_input("enter password :")

x.sendto(user,("",7777))
x.sendto(password,("",7777))

print x.recvfrom(100)
while True:
	cmd=raw_input("[root@localhost ]# ")
	x.sendto(cmd,("",7777))
	print x.recvfrom(100)[0]
