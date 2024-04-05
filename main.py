from key_generator import generate_keys
from encryption import encrypt_message
from decryption import decrypt_message

if __name__ == "__main__":
    public_key_file = "public_key.asc"
    private_key_file = "private_key.asc"
    userid = "ptpmg@hotmail.com"
    encrypted_message_file = "encrypted_message.asc"
    decrypted_message_file = "decrypted_message.txt"
    passphrase = "bora"  # Meter 'None' para não ter password e funcionar, ainda nao esta funcional :(

    generate_keys(public_key_file, private_key_file, userid, passphrase)

    message = "Hello, this is a test message to encrypt."
    encrypt_message(message, public_key_file, encrypted_message_file)
    decrypt_message(encrypted_message_file, private_key_file, decrypted_message_file, passphrase)
    

