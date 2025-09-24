import math

class Circle:
    def __init__(self):
        self.__r=float(input("Enter radius: "))

    def area(self):
        print("Area: ",round(math.pi*self.__r**2,2))
    
    def peri(self):
        print("Perimeter: ",round(2*math.pi*self.__r,2))
    
mycircle=Circle()
mycircle.area()
mycircle.peri()
