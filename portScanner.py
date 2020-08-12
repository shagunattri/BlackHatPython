#!/bin/python3
import sys
import socket
from datetime import datetime

# Define target

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  #Translate hostname to IPV4
else:
    print("Invalid amount of arguments!.\n")
    print("Syntax: python scanner.py <ip>")

# Banner

print("-" * 50)
print("Scanning Target " + target)
print("Time Started: "+str(datetime.now()))
print("-" * 50)

try:
        for port in range(50,65535):
                socket.setdefaulttimeout(1)
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = s.connect_ex((target,port))  # return error indicator
                print("Checking port {}".format(port))
                if result == 0:
                        print("Port {} is open".format(port))
                s.close()

except KeyboardInterrupt:
    print("\n Exiting Program.")
    sys.exit()

except socket.gaierror: 
    print("Hostname could not be resolved.")
    sys.exit()

except socket.error:
    print("Couldn't connect to server.")
    sys.exit()
