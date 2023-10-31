# Task15

# Write some code that uses a list comprehension to create a list called cubes
# that contains the cubed values (x * x * x) of the numbers from 2 to 20 inclusive.

cubes = [x*x*x for x in range(2, 20)]
print(cubes)

# The result: [8, 27, 64, 125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859]