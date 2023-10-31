# Task1

# Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

def to_binary(num):
    if num < 0:
        return
    return bin(num) [2:]

number = 12
binary_representation = to_binary(number)
print(binary_representation)


# Output:
# 1100