# Task5

# Another way to hide a message is to include the letters that make it up within
# seemingly random text. The letters of the message might be every fifth character,
# for example. Write and test a function that does such encryption. It should
# randomly generate an interval (between 2 and 20), space the message out
# accordingly, and should fill the gaps with random letters. The function should
# return the encrypted message and the interval used.
# For example, if the message is "send cheese", the random interval is 2, and for
# clarity the random letters are not random:
# send cheese
# s e n d c h e e s e
# sxyexynxydxy cxyhxyexyexysxye


import random
import string


def main():
    def choice():
        decision = input("\nWould you like to run again? ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    def random_encrypt(message):

        interval = random.randint(2, 20)

        random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(interval - 1))

        encrypted_msg = ''
        for i, char in enumerate(message):
            if char != ' ':
                encrypted_msg += char
            else:
                encrypted_msg += random_letters
                random_letters = ''.join(random.choice(string.ascii_letters) for _ in range(interval - 1))

        encrypted_msg += random_letters

        return encrypted_msg, interval

    original_message = (input("\nPlease type in your message: "))
    encrypted_message, interval = random_encrypt(original_message)
    print(f"Original Message: {original_message}")
    print(f"Encrypted Message: {encrypted_message}")
    print(f"Interval Used: {interval}")

    choice()


main()

# Output:

# Please type in your message: Hello World!
# Original Message: Hello World!
# Encrypted Message: HellomHeTtoINbkWorld!wxLoiWBxCQ
# Interval Used: 11
#
# Would you like to run again? y
#
# Please type in your message: Hello Abby! How are you?
# Original Message: Hello Abby! How are you?
# Encrypted Message: HellovrxAbby!oqDHowFrqareTuwyou?RCu
# Interval Used: 4
#
# Would you like to run again? n
#
# Process finished with exit code 0
