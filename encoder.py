# ANDRES DE LA FLOR


# Encode the password by shifting each character by 3 numbers
def encode(password):
    encoded = ""  # This will be the encoded password

    # Loop through the password to shift each character
    for digit in password:
        shifted = (int(digit) + 3) % 10  # Get the remainder of division by 10 to get the digit it should be
        encoded += str(shifted)

    return encoded

# The main function of the program
def main():
    # The password gets stored in this variable
    password = ""

    on = True
    while on:
        print("Menu \n"
              "------------- \n"
              "1. Encode \n"
              "2. Decode \n"
              "3. Quit")

        # Ask user for input
        choice = int(input("Please enter an option: "))

        # If they asked to encode, encode it
        if choice == 1:
            password = encode(input("Please enter your password to encode: "))
            print("Your password has been encoded and stored!")

        # TODO: Call the decoder, if they asked to decode
        elif choice == 2:
            pass

        # Quit the loop if they ask to quit
        elif choice == 3:
            on = False


if __name__ == '__main__':
    main()
