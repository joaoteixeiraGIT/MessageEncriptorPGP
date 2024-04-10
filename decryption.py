from pgpy import PGPMessage, PGPKey
from pgpy.errors import PGPError

#Esta função desencripta uma mensagem com a chave privada do destinatário
def decrypt_message(encrypted_message_file, private_key_file, decrypted_message_file):
    #Lê a chave privada do ficheiro
    with open(private_key_file, 'rb') as f:
        keys_data = f.read()
    private_key, _ = PGPKey.from_blob(keys_data)
    unlock_passphrase = None #input("Enter the passphrase to unlock the private key: ")
    #Desbloqueia a chave privada
    with private_key.unlock(unlock_passphrase) as unlocked_key:
        if not unlocked_key.is_unlocked:
            print("Failed to unlock key")
            return
    #Lê a mensagem encriptada do ficheiro
    with open(encrypted_message_file, 'rb') as f:
        message_data = f.read()
    encrypted_message = PGPMessage.from_blob(message_data)
    #Desencripta a mensagem
    try:
        decrypted_message = unlocked_key.decrypt(encrypted_message).message
    except PGPError as e:
        print("Failed to decrypt message:", e)
        return

    #Guarda a mensagem desencriptada em ficheiro
    with open(decrypted_message_file, 'wb') as f:
        f.write(decrypted_message.encode())

    print("Message decrypted successfully.")