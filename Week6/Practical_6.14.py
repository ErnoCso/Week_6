# Task14

# Write some code that makes a copy of the colours using the copy() method.
# Then make some changes to the original list.
# Print the contents of the copied list to ensure these changes have not affected the copy.

colours = ["red", "green", "yellow", "blue", "red"]
print(f"This is the original list: {colours}")

new_colours = colours.copy()
print(f"This is a copy of the original list: {new_colours}\n")

colours.remove("green")
print(f"This is the modified list: {colours},\nThis is a copy of the original list  {new_colours}")

# Output:
# This is the original list: ['red', 'green', 'yellow', 'blue', 'red']
# This is a copy of the original list: ['red', 'green', 'yellow', 'blue', 'red']
# 
# This is the modified list: ['red', 'yellow', 'blue', 'red'],
# This is a copy of the original list  ['red', 'green', 'yellow', 'blue', 'red']
