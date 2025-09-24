#a
print("--pattern 1--")
for i in range(5):
    for j in range(i):
        print("*",end="")
    print()

#b
print("--pattern 2--")
for i in range(1,6,2):
    for j in range(i):
        print("*",end="")
    print()
i-=1
while i > 0:
    if i%2!=0:
        for j in reversed(range(i)):
            print("*",end="")
        print()
    i-=1