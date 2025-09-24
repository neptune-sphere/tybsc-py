f=open("demo.txt","r")

ucnt=0
data=f.read()
for ch in data:
        if  ch.isupper():
            ucnt+=1

print("Number of uppercase characters : ",ucnt)
f.close()