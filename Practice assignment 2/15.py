mystr=input('Enter a string: ')
lcnt=0
ncnt=0
for i in mystr:
    if i.isalpha():
        lcnt+=1
    if i.isdigit():
        ncnt+=1
print("letters: ",lcnt,"\nNumbers: ",ncnt)