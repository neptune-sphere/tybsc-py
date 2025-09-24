from datetime import date

class Person:
    def __init__(self):
        self.__name=input("Enter first name:")
        self.__surname=input("Enter last name: ")
        self.__bdate=date(int(input("Enter year: ")),int(input("Enter month: ")),int(input("Enter day: ")))
        self.__addr=input("Enter address: ")
        self.__ph=int(input("Enter phone number: "))
        self.__email=input("Enter email id: ")
       
    def display(self):
        print("Name: ",self.__name,self.__surname,"\nBirthday: ",self.__bdate,"\nAddress: ",self.__addr,"\nPhone Number: ",self.__ph,"\nEmail: ",self.__email)
        self.__myage()

    def __myage(self):
        current=date.today()
        x=current.year-self.__bdate.year - ((current.month,current.day)<(self.__bdate.month,self.__bdate.day))
        print("Current age is :" ,x)
    
        

obj=Person()
print("----User details----")
obj.display()

