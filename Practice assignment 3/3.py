l1=[]
l2=[]


def accept():
    n=int(input("Enter number of elements: "))
    for i in range(n):
       x=input("Enter element: ") 
       l1.append(x)

def unique():
    for i in l1:
        if l1.count(i)==1:
            l2.append(i)   

accept()
unique()

print(l2)