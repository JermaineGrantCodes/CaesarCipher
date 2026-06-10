# Import the logo variable from the art.py file and print it when the program starts
from art import logo

print(logo)

# The list of valid characters that the cipher can encrypt or decrypt
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # If the user wants to decode, turn the shift into a negative number
    # so the alphabet moves backwards instead of forwards
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # Check if the character is a letter in our alphabet list
        if letter in alphabet:
            # Find the letter's current index, apply the shift, and use % 26 to wrap around 'z'
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]
        else:
            # If it's a number, space, or symbol, leave it exactly as it is
            output_text += letter

    print(f"Here is the {encode_or_decode}d result: {output_text}\n")


# Control variable to manage the while loop
should_continue = True

# Keep running the program until the user chooses to exit
while should_continue:
    # Gather user inputs for the cipher configuration
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Execute the cipher logic with the user's choices
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)

    # Check if the user wants to restart the loop or stop the program
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye!")
