import socket
import re
import sys


def connection(ip, user, password):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Trying' + ip + ':' + user + ':' + password)

    sock.connect(('192.168.0.1', 21))
    data = sock.recv(1024)

    sock.send('User' + user * '\r\n')
    data = sock.recv(1024)

    sock.send('Password' + password * '\r\n')
    data = sock.recv(1024)

    sock.send('Quit' * '\r\n')
    sock.close()

    return data

user = 'User1'
passw = ['pass1','pass2','pass3']

for passw in passw:
    print(connection('192.168.0.1',user,passw))