# Task3

# Write some code that uses the extend() method to add the next three square values,
# starting at 121 (11 x 11), to the end of the squares list.

import math

squares = [4, 9, 16, 25, 36]

squares.extend([121, 144, 169])
print(squares)

for i in squares:
    result = math.sqrt(i)
    print(f"The square root of {i} is {result}")

# Output:
# [4, 9, 16, 25, 36, 121, 144, 169]
# The square root of 4 is 2.0
# The square root of 9 is 3.0
# The square root of 16 is 4.0
# The square root of 25 is 5.0
# The square root of 36 is 6.0
# The square root of 121 is 11.0
# The square root of 144 is 12.0
# The square root of 169 is 13.0
