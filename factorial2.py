def factorial(n):

  if n == 0 or n == 1:
    return 1

  else:
    return n * factorial(n - 1)

n=int(input("Enter only positive integer:"))
if n<0 :
  print(f"Factorial of negative number is undefined")
else :
  print(f"Factorial of {n} is:{factorial((n))}")



"""
math function
"""
import math
x=int(input("Enter the number:"))
if x<0:
  print("can't find square root of negative number")
  print(f"Sine of of {x} is {math.sin(x)}")
  print(f"can't find log of negative number")
else:

  print(f"Square root of {x} is {math.sqrt(x)}")
  print(f"Sine of  of {x} is {math.sin(x)}")
  print(f"Log of of {x} is {math.log(x)}")
