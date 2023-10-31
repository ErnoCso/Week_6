# Task2

# Write some code that uses the append() method to add the next three square values
# (49, 64, 81) to the end of the squares list.


import math

squares = [4, 9, 16, 25, 36]

squares.append(49)
squares.append(64)
squares.append(81)

for i in squares:
    result = math.sqrt(i)
    print(result, end="  ")