import socket 

ss=socket.socket()
ss.bind(('',666))
ss.listen()
client,addr=ss.accept()

fname=client.recv(1024)

fname=fname.decode()
try:
    f=open(fname,'r')
    data=f.read()

    client.send(data.encode())
    f.close()
except FileNotFoundError:
    print("Cannot find file!!")
finally:
    client.close()