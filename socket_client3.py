import socket
from time import sleep

def mkline(flags):
  line=''
  for i in range(0,len(flags)):
    if i==0:
      line=str(flags[0])
    else:
      line=line+","+str(flags[i])
  return line

host = '192.168.0.11'
port = 9988

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

flags=[0]*16
while True:
    sleep(2)
    line=mkline(flags)
    s.send(str.encode(line))

s.close()
