import socket
from time import sleep

host = '192.168.0.11'
port = 9988

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    command = input("Enter string: ")
    s.send(str.encode(command))
    if command == 'stop':
      break
#    reply = s.recv(1024)
#    print(reply)

s.close()