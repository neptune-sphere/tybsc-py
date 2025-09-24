import socket

s=socket.socket()
s.connect(('127.0.0.1',666))

fname=input("Enter filename: ")
s.send(fname.encode())

data=s.recv(1024)
print(data.decode())
s.close()

