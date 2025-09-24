import socket

s=socket.socket()
s.connect(('127.0.0.1',777))


data=s.recv(1024)
print("Server: ",data.decode())

while True:
    msg=input('Client:')
    s.send(msg.encode())
    msg1=s.recv(1024)
    print("Server: ",msg1.decode())
    
    if msg1.decode()=='bye':
       
        break
s.close()
    