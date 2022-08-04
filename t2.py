# t2.py

from multiprocessing.connection import Listener

listener = Listener(('192.168.0.7', 16001), authkey=b'password')
print ("listener ready", listener)
running = True
while running :
    print ("ready to connect")
    conn = listener.accept()
    print('connection accepted from', listener.last_accepted)
    msg = conn.recv()
    print("received:", msg)
    conn.send(b"PONG")
