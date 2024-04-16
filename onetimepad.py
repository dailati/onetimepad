import random

def generate_key(ml):
    key = [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(ml)]
    return ''.join(key)

def encrypt(message, key):
    encrypted = ''
    for i in range(len(message)):
        encrypted += chr((ord(message[i]) + ord(key[i])) % 26 + ord('A'))
    return encrypted

def decrypt(encrypted, key):
    decrypted = ''
    for i in range(len(encrypted)):
        decrypted += chr((ord(encrypted[i]) - ord(key[i])) % 26 + ord('A'))
    return decrypted

plaintext = input("Enter the plaintext message: ").upper()

key = generate_key(len(plaintext))

ciphertext = encrypt(plaintext, key)

print(f"Key: {key}")
print(f"Encrypted Message: {ciphertext}")

decrypted = decrypt(ciphertext, key)
print(f"Decrypted Message: {decrypted}")
