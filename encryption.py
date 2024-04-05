from pgpy import PGPKey, PGPMessage
from pgpy.constants import CompressionAlgorithm, SymmetricKeyAlgorithm


def encrypt_message(message, public_key_file, encrypted_message_file):
    keys = PGPKey.from_file(public_key_file)
    if not keys:
        raise ValueError(f"No keys found in {public_key_file}")
    recipient_key = keys[0]

    message = PGPMessage.new(message)

    encrypted_message = recipient_key.encrypt(message, 
                                     cipher=SymmetricKeyAlgorithm.AES256, 
                                     compression=CompressionAlgorithm.Uncompressed)

    with open(encrypted_message_file, 'wb') as f:
        f.write(bytes(encrypted_message))

    print("Message encrypted successfully.")