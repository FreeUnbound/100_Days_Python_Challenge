import ascii_art

print(ascii_art.logo[0])

alphabet =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def ceaser(og_text,shift_amount,encode_or_decode):
    output_text = ""

    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in og_text:
        if letter not in alphabet:
            output_text += letter
        else:

            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)

            output_text += alphabet[shifted_position]

    print(f"Here is your {encode_or_decode}d result: '{output_text}'")

should_continue = True
while should_continue:
    direction = input("Enter 'encode' to encrypt data or 'decode' to decrypt data: \n").lower()
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    ceaser(text,shift,direction)

    restart = input("Would you like to continue? (y/n)\n").lower()
    if restart == "n":
        should_continue = False
        print("Goodbye!")
    else:
        should_continue = True