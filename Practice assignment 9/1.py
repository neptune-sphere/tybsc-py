class CovidError(Exception):
    def __init__(self,x,y):
        self.o=x
        self.sc=y
    
    def __str__(self):
        return "\n----\nPatient is Positive!\nOxygen level:"+str(self.o)+"\nHRCT Score:"+str(self.sc)

class patient:
    def __init__(self):
        self.name=input('Enter name: ')
        self.age=int(input("Enter age: "))
        self.oxy=float(input("Enter oxygen level: "))
        self.score=int(input("Enter HRCT score: "))
        try:
            if(self.oxy < 95.0 or self.score<8):
                raise CovidError(self.oxy,self.score)
            else:
                self.display()
        except CovidError as ce:
            print(ce)
            


        

    def display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Oxygen level: ",self.oxy)
        print("HRCT score: ",self.score)
        print("Patient is Negative!")


obj=patient()

