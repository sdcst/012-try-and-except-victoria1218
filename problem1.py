#python3
# Quadratic Equation
# Have the user enter in the coefficients of a quadratic equation in the
# format: ax^2 + bx + c = 0 and calculate the solutions of the equation
# rounded to 2 decimal places. Use a try...except block to catch if there
# is no solution


""" Sample output:
Enter in the coefficients for a quadratic equation in the format:
  ax^2 + bx + c = 0
a:3
b:d
c:1
Those are not valid values for a, b or c
a:3
b:2
c:1
There are no real roots to the equation
a:2
b:-3
c:-6
The roots are 2.64 and -1.14
a:1
b:8
c:16
The roots are -4.0 and -4.0
"""
import os
os.system('cls')


print("Enter in the coefficients for a quadratic equation in the format:")
print("  ax^2 + bx + c = 0")
a = (input("enter a number for a : "))
b = (input("enter a number for b : "))
c = (input("enter a number for c : "))
import math
try:
    a = float(a)
    b = float(b)
    c = float(c)
    try:
      x = ((-b+math.sqrt(b**2-4*a*c))/(2*a))
      x1 = ((-b-math.sqrt(b**2-4*a*c))/(2*a))
      x = round(x,2)
      x1 = round(x1,2)
      print(f"The roots are {x} and {x1} ")
    except:
       print("There are no roots.")
except:
   print("Those are not valid values for a, b or c")