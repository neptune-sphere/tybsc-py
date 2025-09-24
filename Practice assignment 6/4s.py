import socket

ss=socket.socket()
ss.bind(('',777))
ss.listen()
client,addr=ss.accept()
msg="Start a conversation"
client.send(msg.encode())
    
while True:
    data=client.recv(1024)

    print("Client: ",data.decode())
    msg=input("Server: ")
    client.send(msg.encode())

    if data.decode()=='bye':
        break
client.close()

