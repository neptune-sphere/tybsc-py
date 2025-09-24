l1=[]


def max(l1):
    max=0
    for i in l1:
        if i > max:
            max=i
    print("maximum is : ",max)
    

def accept():
    global l1
    n=int(input("Enter number of integers: "))
    for i in range(n):
        x=int(input("Enter a number: "))    
        l1.append(x)


accept()
max(l1)