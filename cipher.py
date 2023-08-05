def caesar_cipher(text,shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    char_map = {alphabet[i]: shifted_alphabet[i] for i in range(26)}
    encrypted_text = ''

    for char in text:
        if char.lower() in char_map:
            encrypted_char = char_map[char.lower()]
            encrypted_text += encrypted_char.upper() if char.isupper() else encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

text = input("Please enter text to be encrypted:")
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Encryption:", encrypted_text)