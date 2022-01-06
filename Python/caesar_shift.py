# Basic Caesar Cipher Text shifting
# Converts all special chars to SPACE, preserves case
def caesar_shift(plaintext, shift_value):
    output = ""
    
    for character in plaintext:
        if (character.isalpha()):
            if (character.isupper()):
                codepoint = ord(character)
                position = (codepoint - 65) + shift_value
                position = position % 26
                codepoint = position + 65
                output += chr(codepoint)
            else:
                codepoint = ord(character)
                position = (codepoint - 97) + shift_value
                position = position % 26
                codepoint = position + 97
                output += chr(codepoint)
        else:
            output += " "

    return output

def decrypt_check(ciphertext):
    return_format = "Shift Val: {0}, Output: {1}"
    for i in range(26):
        print(return_format.format(i, caesar_shift(ciphertext, -i)))

# Test function
def main():
    message = input("Input String: \n")
    shift_val = int(input("Shift Value: \n"))

    ciphered_string = caesar_shift(message, shift_val)
    deciphered_string = caesar_shift(ciphered_string, -shift_val)

    print("Ciphered String: " + ciphered_string)
    print("Deciphered String: " + deciphered_string)



main()
# decrypt_check()