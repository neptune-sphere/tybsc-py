mystr=input('Enter a string :')
mylist=mystr.split(' ')
print(mylist)

l2=[]
for i in mylist:
    if any(chr.isalpha() for chr in i) and any(chr.isdigit() for chr in i):
        l2.append(i)

print(l2)


