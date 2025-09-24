import socket

from datetime import datetime

usr=input("Enter name : ")
s=socket.socket()
s.connect(('127.0.0.1',6666))

data=s.recv(1024)

datestr=data.decode()
datetime_obj=datetime.strptime(datestr,"%d%b%Y%H%M%S")

time=datetime_obj.time()

h=time.hour

if h>=0 and h<12:
    print("Good morning, ",usr)
elif h>=12 and h<16:
    print("Good afternoon, ",usr)
elif h>=16 and h<19:
    print("Good evening, ",usr)
elif h>=19 and h<24:
    print("Good night, ",usr)

s.close()