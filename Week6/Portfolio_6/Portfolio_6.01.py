# Task1

# Write a function that accepts a positive integer as a parameter and then returns a
# representation of that number in binary (base 2).
# Hint: This is in many ways a trick question. Think!

def main():
    def choice():
        decision = input("Would you like to run again? ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    parameters = int(input("Please type in an integer: "))

    def to_binary(num):
        if num < 0:
            return
        return bin(num)[2:]

    binary_representation = to_binary(parameters)
    print(binary_representation)

    choice()


main()

# Output:

# Please type in an integer: 45
# 101101
# Would you like to run again? y
# Please type in an integer: 67
# 1000011
# Would you like to run again? n
# 
# Process finished with exit code 0
