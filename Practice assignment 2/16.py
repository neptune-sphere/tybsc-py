def even(mylist):
    return mylist%2==0
    
mylist=[1,2,3,4,5,6,7,8,9,10]
x=list(filter(even,mylist))
print(x)