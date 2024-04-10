from pgpy import PGPKey, PGPMessage
from pgpy.constants import CompressionAlgorithm, SymmetricKeyAlgorithm

#Esta função encripta uma mensagem com a chave pública do destinatário
def encrypt_message(message, public_key_file, encrypted_message_file):
    #Lê a chave pública do ficheiro
    keys = PGPKey.from_file(public_key_file)
    #Verifica se a chave foi encontrada
    if not keys:
        raise ValueError(f"No keys found in {public_key_file}")
    #Guarda a chave pública do destinatário
    recipient_key = keys[0]
    #Cria a mensagem
    message = PGPMessage.new(message)
    #Encripta a mensagem
    encrypted_message = recipient_key.encrypt(message, 
                                     cipher=SymmetricKeyAlgorithm.AES256, 
                                     compression=CompressionAlgorithm.Uncompressed)
    #Guarda a mensagem encriptada em ficheiro
    with open(encrypted_message_file, 'wb') as f:
        f.write(bytes(encrypted_message))

    print("Message encrypted successfully.")