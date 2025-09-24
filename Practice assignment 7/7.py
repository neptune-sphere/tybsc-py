import numpy as np
from numpy import random 

arr1 = random.randint(50, size=(10))
arr2 = random.randint(70, size=(10))
print(arr1)
print(arr2)

print('The common element is:',np.intersect1d(arr1,arr2))