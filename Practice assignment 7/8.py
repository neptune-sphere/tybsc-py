import numpy as np
from numpy import random 

arr = random.randint(50,size=(4,4))
print('Array is: \n',arr)
print('reverse all rows: \n',arr[::-1])
print('reverse all columns: \n',arr[::,::-1])
print('reverse array: \n',arr[::-1,::-1])
print('swap two rows: ')
arr[[1,2],:] = arr[[2,1],:]
print(arr)
print('swap two columns: ')
arr[:,[1,2]] = arr[:,[2,1]]
print(arr)