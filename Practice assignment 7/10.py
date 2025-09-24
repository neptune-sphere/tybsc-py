import numpy as np
from numpy import random

arr1 = random.randint(100, size=(3,3))
print('matrix A is:\n',arr1)
arr2 = random.randint(100,size=(3,3))
print('matrix B is:\n',arr2)
print('Addition of matrix A and B is:\n',arr1+arr2)
print('Subtraction of matrix A and B is:\n',arr1-arr2)
print('Multiplication of matrix A and B is:\n',arr1*arr2)
print('Transpose of matrix A is:\n',arr1.transpose())
print('Transpose of matrix B is:\n',arr2.transpose())