import math

try:
    x = float(input("Enter a number: "))
    ans=math.sqrt(x)
    print("square root : ",ans)
except ValueError as ve:
    print(ve)
except ArithmeticError as ae:
    print(ae)