d1={}

def accept():
    global d1
    n=int(input("Enter n:   "))
    for i in range(1,n+1):
        d1[i]=i*i

    val=d1.values()
    print(val)

accept()
