from inputValidation import validate, yes_or_no


def key(plaintext):
    """ Takes a user input for a keyword
    returns that key repeated until same length as plaintext"""
    key_input = validate("Enter a keyword (letters only): ", "A", "U")
    length = len(plaintext)
    key = (key_input * (int(length / len(key_input)) + 1))[:length]
    print(f'Key: {key_input}')
    print(f'Key stretched to:\n'
          f'{key}')
    return key


def encrypt(plaintext, key):
    """Takes plaintext, returns Vignere ciphertext"""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" * 2
    ciphertext = ""
    spaces = False
    if " " in plaintext:
        spaces = yes_or_no("Do you want to have spaces visible in the ciphertext? [Y]/[N]: ")
    for i in range(len(plaintext)):
        letter = plaintext[i]
        if spaces:
            if letter == " ":
                ciphertext += " "
        ciphertext += alphabet[alphabet.find(letter) + alphabet.find(key[i])]
    print("Encrypting...")
    print(f'Plaintext:  {plaintext}.')
    print(f'Ciphertext: {ciphertext}')
    return ciphertext


plaintext = validate("Enter plaintext (letters only): ", "A", "U")
ciphertext = ""
key = key(plaintext)
print("")
print(plaintext)
encrypt(plaintext, key)
# print(key(plaintext))
print(key)