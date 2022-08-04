# t1.py

from multiprocessing.connection import Client
address = ('192.168.0.7', 16001)            
conn = Client(address, authkey = b'password')        
conn.send(b"PING")
print(conn.recv())
