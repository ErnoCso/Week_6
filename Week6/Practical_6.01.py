# Task1

# Write a for..in loop that iterates over all the elements of the squares list and prints
# the square root of each to the screen. Hint: you may want to import a function
# from the math module to help achieve this.

import math

squares = [4, 9, 16, 25, 36]

for i in squares:
    result = math.sqrt(i)
    print(result, end="  ")

# Output:
# 2.0  3.0  4.0  5.0  6.0  
