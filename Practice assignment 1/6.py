import math
r=float(input("Enter radius:"))
h=float(input("Enter height:"))
vol=math.pi * r**2 * h
area=(2*math.pi * r * h) + (2*math.pi * r**2)
print("Volume: ",vol,"\nArea: ",area)
