# Task12

# Write some code that uses the pop() method to remove and display the first value of the squares list.
# Print the list afterward to ensure the value displayed has been removed.

import math

squares = [4, 9, 16, 25, 36, 49, 64, 81, 100]
print(f"                  The original list: {squares}")

squares.reverse()
print(f"The list is after the pop() command: {squares}")

# The result:
#                   The original list: [4, 9, 16, 25, 36, 49, 64, 81, 100]
# The list is after the pop() command: [100, 81, 64, 49, 36, 25, 16, 9, 4]

# An other solution:
# squares[:]=squares[::-1]