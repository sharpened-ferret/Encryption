 # Basic implementation of Vigenere cipher using mod 
 # (with tweak to allow for mismatched key-message lengths, though it's insecure practice)
def vigenere_crypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    ciphertext = []
    for i in range(len(plaintext)):
        key_pos = i % len(key)
        curr = (ord(plaintext[i]) + ord(key[key_pos])) % 26
        curr += 65
        ciphertext.append(chr(curr))
    output = "".join(ciphertext)
    print(output)
    return output

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    plaintext = []
    for i in range(len(ciphertext)):
        key_pos = i % len(key)
        curr = (ord(ciphertext[i]) - ord(key[key_pos]) + 26) % 26
        curr += 65
        plaintext.append(chr(curr))
    print("".join(plaintext))