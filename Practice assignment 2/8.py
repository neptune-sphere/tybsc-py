def mystrlen(mystr):
    cnt=0
    for i in mystr:
        cnt+=1
    print('Length is :',cnt)


def myrev(mystr):
    mystr1="".join(reversed(mystr))
    print(mystr1)

def myconcat(mystr):
    mystr2=input('Enter a string:')
    mystr3=mystr+mystr2
    print(mystr3)

def strcomp(mystr):
    mystr2=input('Enter second string:')
    if mystr>mystr2:
        print(mystr,"is greater")
    elif mystr==mystr2:
        print('Both strings are equal')
    elif mystr2>mystr:
        print(mystr2,'is greater')

mystr=input('Enter first string:')
print('---Length of the string---')
mystrlen(mystr)
print('---Reversing a string---')
myrev(mystr)
print('---concatenate a string---')
myconcat(mystr)
print('---compare two strings---')
strcomp(mystr)
    