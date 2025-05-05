
#task 5 { Calculate Factorial Using a Function }
a=int(input('enter the no :'))
def factorial (a):
 if a<2 :
  return 1
 else :
  return a * factorial(a-1)
result = factorial(a)
print(f'factorial of {a} is {result}')


#task 6 [Using the Math Module for Calculations]
a=int(input("enter the no."))
from math import *
print(f'square root{sqrt(a)}')
print(f'logrithm{log(a)}')
print(f'sine{sin(a)}')
