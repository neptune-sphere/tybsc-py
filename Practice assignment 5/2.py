class Rectangle:
    def __init__(self):
        self.__length=float(input("Enter length: "))
        self.__width=float(input("Enter width: "))
        self.isSquare()

    @property
    def getLength(self):
        return self.__length
    
    @getLength.setter
    def setLength(self,length):
        self.__length=length

    @property
    def getWidth(self):
        return self.__width

    @getWidth.setter
    def setWidth(self,width):
        self.__width=width

    def area(self):
        print("Area: ",self.__length*self.__width)
    
    def isSquare(self):
        if self.__length==self.__width:
            print("It is a Square")
        else :
            print("It is not a Square")


myrect=Rectangle()
myrect.area()