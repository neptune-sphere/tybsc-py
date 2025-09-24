n1,n2,cnt=0,1,0
n=int(input("Enter how many terms: "))
if n<=0:
    print("--")
if n==1:
    print(n1)
if n>=2:
    while cnt<n:
        print(n1)
        seq=n1+n2
        n1=n2
        n2=seq
        cnt+=1
