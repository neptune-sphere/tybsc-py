l1=[]

def duplicates(l1):
    mylist=[]
    for i in l1:
        if l1.count(i)>1:
            mylist.append(i)
    print("Duplicates are : ",set(mylist))

def accept(l1):
    n=int(input("Enter number of elemets: "))
    for i in range(n):
        x=input("Enter element: ")
        l1.append(x)


accept(l1)
print("entered list is : ", l1)
duplicates(l1)
