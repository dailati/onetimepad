import random

def generate_key(message_length):
    key = [random.randint(0, 255) for _ in range(message_length)]
    return key

def encrypt(message, key):
    encrypted_message = ""
    for i in range(len(message)):
        encrypted_char = chr(ord(message[i]) ^ key[i])
        encrypted_message += encrypted_char
    return encrypted_message

def decrypt(encrypted_message, key):
    decrypted_message = ""
    for i in range(len(encrypted_message)):
        decrypted_char = chr(ord(encrypted_message[i]) ^ key[i])
        decrypted_message += decrypted_char
    return decrypted_message

def main():
    message = input("Enter the message to encrypt or decrypt: ")

    choice = input("Enter 'e' to encrypt or 'd' to decrypt: ")

    key = generate_key(len(message))

    if choice == 'e':
        encrypted_message = encrypt(message, key)
        print("Encrypted message:", encrypted_message)
    elif choice == 'd':
        decrypted_message = decrypt(message, key)
        print("Decrypted message:", decrypted_message)
    else:
        print("Invalid choice. Please enter 'e' to encrypt or 'd' to decrypt.")

if __name__ == "__main__":
    main()