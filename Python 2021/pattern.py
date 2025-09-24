n=int(input("Enter a number: "))

print("---pattern 1---")
for i in range(1,n+1) :
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("---pattern 2---")
for i in reversed(range(1,n+1)):
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("---pattern 3---")
for i in range(1,n+1):
    for j in range(1,i+1):
        if((i+j)%2==0):
            print(1,end=' ')
        else :
            print(0,end=' ')
    print()

print("---pattern 4---")
for i in reversed(range(1,n+1)):
    for j in range(1,i+1):
        if((i+j)%2)==0:
            print(0,end=" ")
        else :
            print(1,end=' ')
    print()
            

print("---pattern 5---")
for i in range(1,n+1):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()

print("---pattern 6---")
for i in reversed(range(1,n+1)):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(j,end=' ')
    print()


print("---pattern 7---") 
for i in range(1,n+1):
    x='a'
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)
    print()
  

print("---pattern 8---") 
for i in reversed(range(1,n+1)):
    x='a'
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)
    print()

x='a'
print("---pattern 9---")  
for i in range(1,n+1):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)
    print()

x='a'
print("---pattern 10---")  
for i in reversed(range(1,n+1)):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end=' ')
        x=chr(ord(x)+1)
    print()

x='a'
print("---pattern 11---")  
for i in range(1,n+1):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end='')
        x=chr(ord(x)+1)
    print()

x='a'
print("---pattern 12---")  
for i in reversed(range(1,n+1)):
    for k in range(i,n+1):
        print(end=' ')
    for j in range(1,i+1):
        print(x,end='')
        x=chr(ord(x)+1)
    print()
