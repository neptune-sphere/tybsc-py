from abc import abstractmethod,ABC

#abc stands for abstract base class

class employee(ABC):
    def __init__(self):
        self.fname=input("Enter name: ")
        self.lname=input("Enter last name: ")
        self.salary=0

    @abstractmethod
    def my_sal(self):
        pass

class full_time(employee):
    def my_sal(self):
        self.salary=float(input("Enter salary: "))-float(input("Enter deductions:  "))
        print("CTC is : ",self.salary*12,"per anum.")

class hourly(employee):
    def my_sal(self):
        self.salary=float(input("Enter number of working hours: "))*(float(input("Enter rate per hour: ")))
        print("wage per day is : ",self.salary)

while True:
    print("1.Full time employee\n2.Part time employee\n3.exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        obj=full_time()
        obj.my_sal()
    elif ch==2:
        obj=hourly()
        obj.my_sal()
    elif ch==3:
        break
    else:
        print("Enter valid choice!")

    
        