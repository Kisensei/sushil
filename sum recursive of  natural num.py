# Python program to find the sum of natural using recursive function

def sum_of_natural_number(n):
   if n <= 1:
       return n
   else:
       return n + sum_of_natural_number(n-1)


num = 99

if num < 0:
   print("Enter a positive number")
else:
   print("The sum is",sum_of_natural_number)