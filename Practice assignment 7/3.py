import numpy as np
from numpy import random 

n=int(input("Enter number of elements : "))

arr=random.randint(1,50,size=n)
print(arr)
arr2=arr.reshape(4,3)
print(arr2)