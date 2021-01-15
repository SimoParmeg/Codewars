import string


def is_pangram(s):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in s:
        if char.lower() in alphabet:
            alphabet = alphabet.replace(char.lower(), '')
    return alphabet == ''

print(is_pangram('How quickly daft jumping zebras vex.'))

