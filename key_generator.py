from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm
import os

#Esta função gera as chaves pública e privada e guarda-as em ficheiros
def generate_keys(public_key_file, private_key_file, userid, passphrase = None):
    #Criação da chave
    key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    #Adição do userid à chave
    uid = PGPUID.new(userid)
    #Adição do userid à chave
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications}, hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256], compression=[])
    #Proteção da chave privada com uma passphrase
    if passphrase:
        key.protect(passphrase, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)
    #Guarda a chave pública e privada em ficheiros
    with open(public_key_file, 'w') as f:
        f.write(key.pubkey.__str__())
    #Guarda a chave privada em ficheiro
    with open(private_key_file, 'w') as f:
        f.write(str(key))
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print("Keys generated and saved successfully.")