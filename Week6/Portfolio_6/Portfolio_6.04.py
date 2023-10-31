# Task4

# Computers are commonly used in encryption. A very simple form of encryption
# (more accurately "obfuscation") would be to remove the spaces from a message
# and reverse the resulting string. Write, and test, a function that takes a string
# containing a message and "encrypts" it in this way.

def main():
    def choice():
        decision = input("\nWould you like to run again? ")
        ans1 = ["Yes", "yes", "YES", "y", "Y"]
        if decision in ans1:
            main()
        else:
            exit()

    msg = (input("\nPlease type in your message: "))

    def encrypt(message):
        # Remove spaces from the message
        msg_without_spc = message.replace(" ", "")

        # Reverse the string
        encrypted_msg = msg_without_spc[::-1]

        return encrypted_msg

    encrypted_msg = encrypt(msg)
    print(f"Original Message: {msg}")
    print(f"Encrypted Message: {encrypted_msg}")

    choice()


main()

# Output:

# Please type in your message: This is a message
# Original Message: This is a message
# Encrypted Message: egassemasisihT
#
# Would you like to run again? y
#
# Please type in your message: This is a secret password
# Original Message: This is a secret password
# Encrypted Message: drowssaptercesasisihT
#
# Would you like to run again? n
#
# Process finished with exit code 0