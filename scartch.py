
import ecdsa

# Generate six pairs of public and private keys for users
users = [ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) for _ in range(6)]
for i in users :
    print(i.verifying_key)