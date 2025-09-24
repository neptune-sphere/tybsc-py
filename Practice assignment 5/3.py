# import math

# class Point:
#     def __init__(self,a,b):
#         self.__x=a
#         self.__y=b
        

#     @staticmethod
#     def distance(p1,p2):
#         d=math.sqrt((p2.__x-p1.__x)**2 + (p2.__y-p1.__y)**2)
#         print("Distance is: ",d)


# a=float(input("Enter X: "))
# b=float(input("Enter Y: "))
# p1=Point(a,b)

# a=float(input("Enter X: "))
# b=float(input("Enter Y: "))
# p2=Point(a,b)

# Point.distance(p1,p2)


import math

class Point:
    x1=0
    x2=0
    y1=0
    y2=0
    distance=0

    def __init__(self,x1,x2,y1,y2):
        self.x1=x1
        self.x2=x2
        self.y1=y1
        self.y2=y2

    def calc_dist(self):
        self.distance=math.sqrt((self.x2-self.x1)**2 + (self.y2-self.y1)**2)
        print("Distance between two points is : ",self.distance)

x1 = float(input("Enter x1 : "))
x2 = float(input("Enter x2 : "))
y1 = float(input("Enter y1 : "))
y2 = float(input("Enter y2 : "))

p=Point(x1,x2,y1,y2)

p.calc_dist()

