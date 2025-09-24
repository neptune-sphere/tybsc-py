def squares(x):
    return x*x

l1=[i for i in range(10)]
l2=list(map(squares,l1))
print("",l2)