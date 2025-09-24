class Printer:
    def setString(self,x):
        self.__mystr=x
    
    def printString(self,ch):
        if ch in 'Uu':
            print(self.__mystr.upper())
        if ch in 'Ll':
            print(self.__mystr.lower())


obj=Printer()
temp=input("Enter a string: ")

obj.setString(temp)
choice=input("Enter upper or lower (u/l): ")
obj.printString(choice)
