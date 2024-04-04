from pgpy import PGPMessage, PGPKey
from pgpy.errors import PGPError

def decrypt_message(encrypted_message_file, recipient_private_key_file, decrypted_message_file, passphrase=None):
    keys = PGPKey.from_file(recipient_private_key_file)
    if not keys:
        raise ValueError(f"No keys found in {recipient_private_key_file}")
    recipient_key = keys[0]

    if passphrase:
        try:
            recipient_key.unlock(passphrase)
        except PGPError as e:
            print("Failed to unlock private key:", e)
            return

    if not recipient_key.is_unlocked:
        print("Failed to unlock private key with provided passphrase.")
        return

    message = PGPMessage.from_file(encrypted_message_file)

    decrypted_message = recipient_key.decrypt(message)

    with open(decrypted_message_file, 'w') as f:
        f.write(str(decrypted_message.message))

    print("Message decrypted successfully.")