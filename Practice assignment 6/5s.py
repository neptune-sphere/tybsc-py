import socket



class student:
    def __init__(self):
        self.name=input("Enter student name: ")
        self.roll=int(input("Enter roll no: "))
        self.mks=float(input("Enter marks: "))
    
    def display(self):
        print("Name: ",self.name)
        print("Roll number: ",self.roll)
        print("Marks: ",self.mks)
    
    def __repr__(self):
        return 'name: '+self.name+'\troll: '+str(self.roll)+'\tmks:'+str(self.mks)

ob=student()
# ob.display()
mydata=ob.__repr__()


ss=socket.socket()
ss.bind(('',777))
ss.listen()
client,addr=ss.accept()

client.send(mydata.encode())
client.close()
