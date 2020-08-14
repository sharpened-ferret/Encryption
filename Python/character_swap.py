# Ciphers text with char swap dictionary
def dict_char_swap_crypt(plaintext_string):
    output = ""
    swap_dict = {"a": "c", "b": "z", "c": "u", "d": "d", "e": "a", "f": "l", "g": "s", "h": "m", "i": "k", "j": "w", "k": "n", "l": "y", "m": "x", "n": "b", "o": "o", "p": "e", "q": "j", "r": "g", "s": "f", "t": "h", "u": "v", "v": "i", "w": "p", "z": "t", "x": "q", "y": "r"}
    plaintext_string = plaintext_string.lower()


    for character in plaintext_string:
        output += swap_dict.get(character, " ")
    
    return output

# Deciphers text with reversed dictionary
def dict_char_swap_decrypt(ciphered_string):
    output = ""
    decipher_dict = {'c': 'a', 'z': 'b', 'u': 'c', 'd': 'd', 'a': 'e', 'l': 'f', 's': 'g', 'm': 'h', 'k': 'i', 'w': 'j', 'n': 'k', 'y': 'l', 'x': 'm', 'b': 'n', 'o': 'o', 'e': 'p', 'j': 'q', 'g': 'r', 'f': 's', 'h': 't', 'v': 'u', 'i': 'v', 'p': 'w', 't': 'z', 'q': 'x', 'r': 'y'}
    ciphered_string = ciphered_string.lower()

    for character in ciphered_string:
        output += decipher_dict.get(character, " ")
    
    return output


# Test function
def main():
    user_input = input("Input String: \n")

    ciphered_string = dict_char_swap_crypt(user_input)
    deciphered_string = dict_char_swap_decrypt(ciphered_string)

    print("Ciphered String: " + ciphered_string)
    print("Deciphered String: " + deciphered_string)

main()