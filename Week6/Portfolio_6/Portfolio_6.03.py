# Task3

# Write and test a function that determines if a given integer is a prime number. A
# prime number is an integer greater than 1 that cannot be produced by multiplying
# two other integers.

def main():
    def choice():
        decision = input("\nWould you like to run again?Y/N ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    num = int(input("\nPlease type in an integer: "))
    def prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True

        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6

        return True

    if prime(num):
        print(f"The integer {num} is a prime number.")
    else:
        print(f"The integer {num} is not a prime number.")

    choice()

main()

# Output:

# Please type in an integer: 11
# The integer 11 is a prime number.
#
# Would you like to run again?Y/N Y
#
# Please type in an integer: 21
# The integer 21 is not a prime number.
#
# Would you like to run again?Y/N yes
#
# Please type in an integer: 123
# The integer 123 is not a prime number.
#
# Would you like to run again?Y/N no
#
# Process finished with exit code 0