flag=0

mystr=input('Enter a string: ')
mystr=mystr.lower()

vowels={'a':mystr.count('a'),'e':mystr.count('e'),'i':mystr.count('i'),'o':mystr.count('o'),'u':mystr.count('u')}
print(vowels)

countvalues=vowels.values()
print(countvalues)

for i in countvalues:
    if i == 0:
        flag=1
        break

if flag==1:
    print('Unacceptable')
else:
    print('Understabdable, have a nice day')
