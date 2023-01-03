#You have been given a positive integer N. You need to find and print the Factorial of this number. The factorial of a positive integer N refers to the product of all number on the range from 1 to N. 

n = int(input())

def factorial(n):
  if n == 1:
    return n
  else:
    return n * factorial(n - 1)
  
print(factorial(n))
