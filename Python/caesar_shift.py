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

# Test function
def main():
    user_input = input("Input String: \n")

    ciphered_string = caesar_shift(user_input, 14)
    deciphered_string = caesar_shift(ciphered_string, -14)

    print("Ciphered String: " + ciphered_string)
    print("Deciphered String: " + deciphered_string)

main()