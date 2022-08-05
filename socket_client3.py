import socket
from time import sleep

def mkline(flags):  # pack flags as a line
  line=''
  for i in range(0,len(flags)):
    if i==0:
      line=str(flags[0])
    else:
      line=line+","+str(flags[i])
  return line

host = '192.168.0.11'   # server ip address
port = 9988

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # establish socket connection
s.connect((host, port))

flags=[0]*16
i=0
while True:   # sending flags via socket
    sleep(2)
    i=i+1
    flags[0]=i % 10
    line=mkline(flags)
    s.send(str.encode(line))
