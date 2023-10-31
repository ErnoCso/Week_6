# Task6

# Write some code that uses the remove() method to remove the value 3 from the squares list.
# Notice how an error is generated since the given value was not present.

import math

squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)

squares.remove(3)
print(squares)

# Output:
# [4, 9, 16, 25, 36, 49, 64, 81, 100]
# [4, 9, 16, 25, 36, 64, 81, 100]
