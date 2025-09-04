alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

#TODO-2: Inside the function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.

# def encrypt(original_text, shift_ammount):
#     cipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) + shift_ammount
#         if shifted_position > 25:
#             shifted_position = shifted_position - 26
#             cipher_text += alphabet[shifted_position]
#         else:
#             cipher_text += alphabet[shifted_position]
        
#     print(f"The encoded text is {cipher_text}")

# def decrypt(original_text, shift_ammount):
#     decipher_text = ""
#     for letter in original_text:
#         shifted_position = alphabet.index(letter) - shift_ammount
#         if shifted_position < 0:
#             shifted_position = shifted_position + 26
#             decipher_text += alphabet[shifted_position]
#         else:
#             decipher_text += alphabet[shifted_position]
        
#     print(f"The decoded text is {decipher_text}")

def ceaser(original_text, shift_ammount, encode_decode_direction):
    output_text = ""
    if encode_decode_direction == "decode":
            shift_ammount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_ammount
        if shifted_position < 0:
            shifted_position = shifted_position + 26
            output_text += alphabet[shifted_position]
        else:
            output_text += alphabet[shifted_position]
        
    print(f"The {encode_decode_direction}d text is {output_text}")

print("Welcome to the Ceaser Cipher")
should_continue = True
while should_continue:
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if result == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
        text = input("Type your message:\n").upper()
        shift = int(input("Type the shift number:\n"))
        ceaser(original_text= text, shift_ammount= shift, encode_decode_direction = direction)
    else:
        should_continue = False
        print("Goodbye")

# encrypt(text, shift)
# decrypt(text, shift)
    

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code to encrypt a message.

#TODO-4: Try