def largest(mylist):
    max=0
    for i in mylist:
        if(i>max):
            max=i
    return max



n=int(input('Enter number of elements : '))
mylist=[int(input('Enter element: ')) for i in range(0,n)]

print(mylist)

print('largest element is : ',largest(mylist))




# mylist=[]
# for i in range(0,n):
#     x=int(input('Enter Element : '))
#     mylist.append(x)
