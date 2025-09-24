from tkinter import E


class triangle():
    def __init__(self,angle1,angle2,angle3):
        self.angle1=angle1
        self.angle2=angle2
        self.angle3=angle3
        self.number_of_sides=3

    def check_angles(self):
        self.tot=self.angle1+self.angle2+self.angle3
        if self.tot==180.0:
            return True
        else:
            return False

x = float(input("First angle:"))
y = float(input("Second angle:"))
z = float(input("Third angle:"))

my_triangle=triangle(x,y,z)

print("Number of sides: ",my_triangle.number_of_sides)
print("Check angles: ",my_triangle.check_angles())

