f=open("demo.txt","r")
lcnt,wcnt,ccnt=0,0,0

data=f.readlines()

lcnt=len(data)

print(lcnt)

for l in data:
    ccnt+=len(l)
    words=l.split()
    wcnt+=len(words)
print(wcnt)
print(ccnt)