# Task5

# Write some code that uses the remove() method to remove the value 49 from the squares list.
# Print the list afterward to ensure the value has indeed been removed.

import math

squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
print(squares)

squares.remove(49)
print(squares)

# Output:
# [4, 9, 16, 25, 36, 49, 64, 81, 100]
# [4, 9, 16, 25, 36, 64, 81, 100]
