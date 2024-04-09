from pgpy import PGPMessage, PGPKey
from pgpy.errors import PGPError

def decrypt_message(encrypted_message_file, private_key_file, decrypted_message_file):
    # Load the private key from the file
    with open(private_key_file, 'rb') as f:
        keys_data = f.read()
    private_key, _ = PGPKey.from_blob(keys_data)
    unlock_passphrase = None #input("Enter the passphrase to unlock the private key: ")

    #Unlock the key
    with private_key.unlock(unlock_passphrase) as unlocked_key:
        if not unlocked_key.is_unlocked:
            print("Failed to unlock key")
            return

    # Load the encrypted message
    with open(encrypted_message_file, 'rb') as f:
        message_data = f.read()
    encrypted_message = PGPMessage.from_blob(message_data)

    # Decrypt the message
    try:
        decrypted_message = unlocked_key.decrypt(encrypted_message).message
    except PGPError as e:
        print("Failed to decrypt message:", e)
        return

    # Write the decrypted message to the file
    with open(decrypted_message_file, 'wb') as f:
        f.write(decrypted_message.encode())

    print("Message decrypted successfully.")