letters = 'abcdefghijklmnopqrstuvwxyz'  # Define the letters of the alphabet
num_letters = len(letters)  # Calculate the number of letters

def encrypt_decrypt(text, mode, key):
    result = ''  # Initialize an empty string to store the result
    if mode == 'd':
        key = -key  # If decryption mode is selected, negate the key to reverse the encryption
      
    for letter in text:
        letter = letter.lower()  # Convert the letter to lowercase
        if not letter == ' ':
            index = letters.find(letter)  # Find the index of the letter in the alphabet
            if index == -1:
                result += letter  # If the letter is not found in the alphabet, add it as is
            else:
                new_index = index + key  # Apply the key to shift the index
                if new_index >= num_letters:
                    new_index -= num_letters  # Wrap around to the beginning of the alphabet if needed
                elif new_index < 0: 
                    new_index += num_letters  # Wrap around to the end of the alphabet if needed
                result += letters[new_index]  # Add the new letter to the result
        else:
            result += ' '  # If the character is a space, add it to the result without encryption/decryption
    return result


print()
print('*** CAESAR CIPHER PROGRAM ***')
print()

print('Do you want to encrypt or decrypt?')
user_input = input('e/d: ').lower()  # Prompt the user for encryption or decryption mode
print()

if user_input == 'e':
    print('ENCRYPTION MODE SELECTED')
    print()
    key = int(input('Enter The Key (1 through 26): '))  # Prompt the user for the encryption key
    text = input('Enter the text to encrypt: ')  # Prompt the user for the text to encrypt
    ciphertext = encrypt_decrypt(text, user_input, key)  # Encrypt the text using the provided key
    print(f'CIPHERTEXT: {ciphertext}')  # Print the encrypted ciphertext
   
elif user_input == 'd':
    print('DECRYPTION MODE SELECTED')
    print()
    key = int(input('Enter The Key (1 through 26): '))  # Prompt the user for the decryption key
    text = input('Enter the text to decrypt: ')  # Prompt the user for the text to decrypt
    plaintext = encrypt_decrypt(text, user_input, key)  # Decrypt the text using the provided key
    print(f'PLAINTEXT: {plaintext}')  # Print the decrypted plaintext
