f=open("demo.txt","r")

for mylist in f:
    print(mylist[::-1])

f.close()