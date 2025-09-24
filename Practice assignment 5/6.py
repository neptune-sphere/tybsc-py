class vehicle:
    def __init__(self):
        self.max_speed=float(input("Enter max speed : "))
        self.mileage=float(input("Enter mileage : "))
        

class bus(vehicle):
    def seating_capacity(self,x=50):
        if x > 50 or x < 0:
            self.capacity=0
        else :
            self.capacity=x
        

    def setfare(self):

        self.fare=((self.capacity*100)/5)+((self.capacity*100)/5)*0.1
        return self.fare

class taxi(vehicle):
    def seating_capacity(self,x=3):
        if x > 3 or x < 0:
            self.capacity=0
        else:
            self.capacity=x

    def setfare(self):
        self.fare=((self.capacity*100)/5)
        return self.fare

while True:
    print("Enter travelling mode: \n1. Taxi \n 2. Bus \n3. Exit")
    ch=int(input("Enter choice: "))

    if ch==1:

        obj=taxi()
        obj.seating_capacity(int(input("Enter no of seats for taxi: ")))
        print("per kilometer charge : ",obj.setfare())
        print("for 100 km total fare for taxi will be : ",100*obj.setfare())
    
    elif ch==2:
        obj=bus()
        obj.seating_capacity(int(input("Enter no of seats for bus: ")))
        print("per kilometer charge : ",obj.setfare())
        print("for 100 km total fare for bus will be : ",100*obj.setfare())

    elif ch==3:
        break
    
    else:
        print("invalid choice!")




