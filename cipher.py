def caesar_cipher(text,shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    mapping = dict(zip(alphabet, shifted_alphabet))

    encrypted_text = ''
    for char in text:
        if char.lower() in mapping:
            if char.isupper():
                encrypted_text += mapping[char.lower()].upper()
            else:
                encrypted_text += mapping[char]
        else:
            encrypted_text += char
    return encrypted_text

text = input("Please enter text to be encrypted:")
shift = 5
encrypted_text = caesar_cipher(text, shift)
print("Encryption:", encrypted_text)                