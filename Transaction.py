import hashlib
import ecdsa
from User import Tx


# Define a simple Transaction class
class Transaction:
    def __init__(self, txins, txouts, amount, signature,prev_transaction_hash=None):
        self.txins = txins
        self.txouts = txouts
        self.amount = amount
        self.prev_transaction_hash = prev_transaction_hash
        self.signature = signature

    def id(self):
        return hashlib.blake2b(self).hexdigest()


    def get_transaction_data(self):
        return f"{self.txins}{self.txouts}{self.amount}{self.prev_transaction_hash}".encode()

    def is_valid(self):
        public_key = self.txins[0].txouts[0][0]
        return public_key.verify(public_key,hashlib.sha256(Tx(self.txins,self.txouts,self.amount).encode()).digest(),self.signature)