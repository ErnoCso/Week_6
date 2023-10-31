# Task3

# Write some code that uses the extend() method to add the next three square values,
# starting at 121 (11 x 11), to the end of the squares list.

import math

squares = [4, 9, 16, 25, 36]

squares.extend([121, 144, 169])

for i in squares:
    result = math.sqrt(i)
    print(f"The square root of {i} is {result}")