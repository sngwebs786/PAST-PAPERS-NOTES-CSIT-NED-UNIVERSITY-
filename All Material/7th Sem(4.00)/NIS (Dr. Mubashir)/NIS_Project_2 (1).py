from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def des_encrypt(plaintext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    padded_plaintext = pad(plaintext.encode(), DES.block_size)
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = cipher.decrypt(ciphertext)
    plaintext = unpad(decrypted_data, DES.block_size)
    return plaintext.decode()

if __name__ == "__main__":
    # Example usage
    key = get_random_bytes(8)  # 8 bytes key for DES
    plaintext = "Network and Informtion Security is so crucial subject in terms of  understanding"

    # Encryption
    encrypted_data = des_encrypt(plaintext, key)
    print("Encrypted:", encrypted_data.hex())

    # Decryption
    decrypted_text = des_decrypt(encrypted_data, key)
    print("Decrypted:", decrypted_text)
