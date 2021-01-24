#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Simple encryption | ----\n", fg("red")))

# user interaction
word = input("Word to encrypt: ").lower()

# variables
suffix = "aca"

# encryption/decryption standard
standard = {
    "a": "0",
    "e": "1",
    "i": "2",
    "o": "2",
    "u": "4"
}

# functions
def encrypt(string):
    encrypted_string = ""
    for i in string[::-1]:
        try:
            encrypted_string += standard[i]
        except:
            encrypted_string += i

    return encrypted_string + suffix

# output
encrypted_word = stylize(encrypt(word), fg("red"))
print(f"\n\"{word}\" encrypted with the Karaca's algorithm is: {encrypted_word}.\n")
