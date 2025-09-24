def hash_display(data):
    mystr=""
    for ch in data:
        mystr+=ch+"#"
    print(mystr)

f=open("demo.txt","r")

data=f.read()
hash_display(data)
f.close()