# Task9

# Write some code that uses the pop() method to remove and display the first value of the squares list.
# Print the list afterward to ensure the value displayed has been removed.

import math

squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"                  The original list: {squares}")

squares.pop(0)
print(f"The list is after the pop() command:    {squares}")

# Output:
#                   The original list: [4, 9, 16, 25, 36, 49, 64, 81, 100]
# The list is after the pop() command:    [9, 16, 25, 36, 49, 64, 81, 100]
