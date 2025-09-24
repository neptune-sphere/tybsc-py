import calendar
x=int(input("Enter year:"))
if(calendar.isleap(x)==True):
    print(x,"is a leap year")
else:
    print(x,"is not a leap year")