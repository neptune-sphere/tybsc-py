import socket
import pickle

s=socket.socket()
hostname=socket.gethostname()
portno=50000
s.bind((hostname,portno))

s.listen(5)
print('server is waiting...')

while True:
    conn,addr=s.accept()
    print("Connection from: " + str(addr))

    class student:
        def __init__(self,fnm,lnm,rno):
            self.fname=fnm
            self.lname=lnm
            self.rollno=rno

        def display(self):
            print("First name: ",self.fname)
            print("Last name: ",self.lname)
            print("Roll no: ",self.rollno)

    fnm=input("Enter first name:")
    lnm=input("Enter last name:")
    rno=input("Enter roll no:")
    s1=student(fnm,lnm,rno)
    std_data={"First name":fnm,"Last name":lnm,"Roll no":rno}
    std=pickle.dumps(std_data)
    conn.send(bytes(std))
    conn.close()
    break
s.close()