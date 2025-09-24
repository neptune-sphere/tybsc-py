import time
import socket

ss=socket.socket()
ss.bind(("",7777))
ss.listen()

client,addr=ss.accept()

currenttime=time.ctime(time.time())+'\r\n'

client.send(currenttime.encode())


