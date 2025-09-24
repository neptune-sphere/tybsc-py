import numpy as np
from numpy import random 

arr1 = random.randint(50,size=(3,3))
print('Original array  :\n',arr1)
n = random.randint(1,9,size=1)
print('Each elemenet of \n',arr1,'\n will be multiplied by : ',n)

print('Array after multiplication is:\n',arr1*n)