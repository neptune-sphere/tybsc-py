mystr=input('Enter a string: ')
str2=''
for i in mystr:
    if i.isalnum():
        str2+=i
print(str2)
