import socket
from time import sleep

host = '192.168.0.11'
port = 9988

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter command: ")
    if command == 'KILL':
        s.send(str.encode(command))
        break
    s.send(str.encode(command))
    reply = s.recv(1024)
    print(reply)

s.close()