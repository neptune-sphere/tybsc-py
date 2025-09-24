import socket
import time
s=socket.socket()

s.connect(('127.0.0.1',777))
time.sleep(5)
mydata=s.recv(1024)

print(mydata.decode())
s.close()