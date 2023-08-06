def caesar_cipher(text,shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    char_map = {alphabet[i]: shifted_alphabet[i] for i in range(26)}
    encrypted_text = ''

    for char in text:
        if char.lower() in char_map:
            encrypted_char = char_map[char.lower()]
            encrypted_text += encrypted_char.lower() if char.isupper() else encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

shift = 5
text = input("Please enter sentence to be encrypted:")
encrypted_text = caesar_cipher(text, shift)
print("The encrypted sentence is:", encrypted_text)