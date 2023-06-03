import base64
from Crypto.Cipher import DES

def pad_text(text):
    # Pad the text to be a multiple of 8 bytes
    padding = 8 - (len(text) % 8)
    return text + padding * chr(padding)

def des_encrypt(key, plaintext):
    # Pad the plaintext
    plaintext = pad_text(plaintext)

    # Create a DES cipher object with the provided key
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext.encode())

    # Encode the ciphertext in base64 for better representation
    encoded_ciphertext = base64.b64encode(ciphertext)

    return encoded_ciphertext.decode()

def des_decrypt(key, ciphertext):
    # Create a DES cipher object with the provided key
    cipher = DES.new(key, DES.MODE_ECB)

    # Decode the ciphertext from base64
    decoded_ciphertext = base64.b64decode(ciphertext)

    # Decrypt the ciphertext
    decrypted_text = cipher.decrypt(decoded_ciphertext)

    # Remove the padding from the decrypted text
    padding = decrypted_text[-1]
    decrypted_text = decrypted_text[:-padding].decode()

    return decrypted_text

# Get user input for key, plaintext, and choice
key = input("Enter the key (8 characters): ").encode()
plaintext = input("Enter the plaintext: ")
choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")

if choice == 'e':
    encrypted = des_encrypt(key, plaintext)
    print("Encrypted ciphertext:", encrypted)
elif choice == 'd':
    decrypted = des_decrypt(key, plaintext)
    print("Decrypted plaintext:", decrypted)
else:
    print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")
