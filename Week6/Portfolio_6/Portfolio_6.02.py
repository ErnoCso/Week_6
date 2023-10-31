# Task2

# Write and test a function that takes an integer as its parameter and returns the
# factors of that integer. (A factor is an integer which can be multiplied by another to
# yield the original).

def main():
    def choice():
        decision = input("\nWould you like to run again? ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    number = int(input("\nPlease type in an integer: "))

    def find_factors(n):
        factors = []
        for i in range(1, n + 1):
            if n % i == 0:
                factors.append(i)
        return factors

    result = find_factors(number)
    print(f"The factors of {number} are: {result}")

    choice()


main()


# Output:

# Please type in an integer: 4
# The factors of 4 are: [1, 2, 4]
#
# Would you like to run again? y
#
# Please type in an integer: 7
# The factors of 7 are: [1, 7]
#
# Would you like to run again? YES
#
# Please type in an integer: 12
# The factors of 12 are: [1, 2, 3, 4, 6, 12]
#
# Would you like to run again? n
#
# Process finished with exit code 0