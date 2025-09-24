import socket 

s=socket.socket()

s.connect(('127.0.0.1',7777))

data=s.recv(1024)

print(data.decode())
s.close()