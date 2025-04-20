from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import os
import base64

# AES Encryption Function
def aes_encrypt(plaintext, key):
    iv = os.urandom(16)  # Generate a random Initialization Vector (IV)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(plaintext.encode()) + encryptor.finalize()
    return iv + ciphertext

# AES Decryption Function
def aes_decrypt(ciphertext, key):
    iv = ciphertext[:16]
    actual_ciphertext = ciphertext[16:]
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_text = decryptor.update(actual_ciphertext) + decryptor.finalize()
    return decrypted_text.decode()

# Key generation (256-bit key)
key = os.urandom(32)
plaintext = "This is a secret message."

# Encrypt the message
ciphertext = aes_encrypt(plaintext, key)
encoded_ciphertext = base64.b64encode(ciphertext).decode()
print("Ciphertext (Base64):", encoded_ciphertext)

# Decrypt the message
decoded_ciphertext = base64.b64decode(encoded_ciphertext)
decrypted_text = aes_decrypt(decoded_ciphertext, key)
print("Decrypted Text:", decrypted_text)
