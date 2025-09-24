class UsernameError(Exception):
    def __init__(self,x):
        self.u=x
    def __str__(self):
        return self.u+"is an invalid username!"

class PasswordError(Exception):
    def __init__(self,x):
        self.p=x
    def __str__(self):
        return self.p+"is an invalid password!"

class user:
  
    def __init__(self):
        
        self.uname=input("Enter username: ")
        try:
            if len(self.uname)<=3:
                raise UsernameError(self.uname)
        except UsernameError as ue:
                print(ue)
                self.uname='user1'
        self.pwd=input("Enter password:")
        try:
            if(len(self.pwd)<8 or self.pwd.isalnum()==False):
                raise PasswordError(self.pwd)
        except PasswordError as pe:
                print(pe)
                self.pwd="occeanic12"
        
        self.display()


            

    def display(self):
        print("Username : ",self.uname,"\nPassword : ",self.pwd)


ob=user()