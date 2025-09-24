n=int(input("Enter a number: "))
ans=0
while n>0:
    d=n%10
    ans+=d
    n//=10
print("sum of digots is",int(ans))

