from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm, SymmetricKeyAlgorithm

def generate_keys(public_key_file, private_key_file, userid, passphrase = None):
    key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 4096)
    uid = PGPUID.new(userid)
    key.add_uid(uid, usage={KeyFlags.Sign, KeyFlags.EncryptCommunications}, hashes=[HashAlgorithm.SHA256], ciphers=[SymmetricKeyAlgorithm.AES256], compression=[])

    if passphrase:
        key.protect(passphrase, SymmetricKeyAlgorithm.AES256, HashAlgorithm.SHA256)

    with open(public_key_file, 'w') as f:
        f.write(key.pubkey.__str__())

    with open(private_key_file, 'w') as f:
        f.write(str(key))

    print("Keys generated and saved successfully.")