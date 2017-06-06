#!/usr/bin/python
def add(x,y):
	print x+y
def clear():
	print "\n"*50
def msg():
	print "hello world"
	import os
	m=raw_input("Enter something to google to search : ")
	os.system("firefox https://www.google.com/search?q="+m)

