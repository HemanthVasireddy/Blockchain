import hashlib
import ecdsa


# Define a simple Transaction class
class Transaction:
    def __init__(self, sender, recipient, amount, prev_transaction_hash=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.prev_transaction_hash = prev_transaction_hash
        self.signature = None

    def sign_transaction(self, private_key):
        private_key = ecdsa.SigningKey.from_string(bytes.fromhex(private_key), curve=ecdsa.SECP256k1)
        self.signature = private_key.sign(self.get_transaction_data())

    def get_transaction_data(self):
        return f"{self.sender}{self.recipient}{self.amount}".encode()

    def is_valid(self):
        if not self.signature:
            return False
        public_key = ecdsa.VerifyingKey.from_string(bytes.fromhex(self.sender), curve=ecdsa.SECP256k1)
        return public_key.verify(self.signature, self.get_transaction_data())