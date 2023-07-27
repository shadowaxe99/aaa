```python
from cryptography.fernet import Fernet

class EncryptionManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)

    def encrypt_data(self, data):
        cipher_text = self.cipher_suite.encrypt(data.encode())
        return cipher_text

    def decrypt_data(self, cipher_text):
        plain_text = self.cipher_suite.decrypt(cipher_text)
        return plain_text.decode()

if __name__ == "__main__":
    manager = EncryptionManager()
    encrypted_data = manager.encrypt_data("Sensitive Data")
    print("Encrypted Data: ", encrypted_data)
    decrypted_data = manager.decrypt_data(encrypted_data)
    print("Decrypted Data: ", decrypted_data)
```