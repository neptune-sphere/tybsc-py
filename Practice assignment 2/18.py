mytup=(1,2,3,4,5,6,7,8,9,10)

for i in range (1,int(len(mytup)/2)+1):
    print(i,end=' ')

print()

i+=1
for j in range(i,int(len(mytup))+1):
    print(j,end=' ')