import socket
from datetime import datetime


currenttime=datetime.now()

timestring=currenttime.strftime("%d%b%Y%H%M%S")

ss=socket.socket()
ss.bind(('',6666))
ss.listen()

client,addr=ss.accept()

client.send(timestring.encode())
client.close()