from key_generator import generate_keys
from encryption import encrypt_message
from decryption import decrypt_message

if __name__ == "__main__":
    public_key_file = "public_key.asc"
    private_key_file = "private_key.asc"
    userid = "ptpmg@hotmail.com"
    recipient_public_key_file = "public_key.asc"
    recipient_private_key_file = "private_key.asc"
    encrypted_message_file = "encrypted_message.asc"
    decrypted_message_file = "decrypted_message.txt"
    passphrase = None  # Set passphrase if the private key is protected

    # Generate keys
    generate_keys(public_key_file, private_key_file, userid, passphrase)

    # Encrypt message
    message = "Hello, this is a test message to encrypt."
    encrypt_message(message, recipient_public_key_file, encrypted_message_file)

    # Decrypt message
    decrypt_message(encrypted_message_file, recipient_private_key_file, decrypted_message_file, passphrase)
    

