import math

a=int(input("Enter a number: "))
if(a<=0):
    print("it is neither even nor odd")
else:
    if(a%2==0):
        print(a,"is even")
    else:
        print(a,"is odd")
