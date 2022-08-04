import socket
import time

host = '192.168.0.11'
port = 9988

def setupServer():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)   #reuse address
    print("Socket created.")
    try:
        s.bind((host, port))
    except socket.error as msg:
        print(msg)
    print("Socket bind complete.")
    return s

def setupConnection():
    s.listen(1) # Allows one connection at a time.
    conn, address = s.accept()
    print("Connected to: " + address[0] + ":" + str(address[1]))
    return conn

def dataTransfer(conn):
    while True:
        data = conn.recv(1024) # receive the data
        data = data.decode('utf-8')
        print(data)
        if data == "stop":
          break
#        conn.sendall(reply)
    conn.close()
    exit()

s = setupServer()

while True:
#    try:
        conn = setupConnection()
        dataTransfer(conn)
#    except:
#        break
