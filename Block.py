
import hashlib
import ecdsa



# Define a simple Block class
class Block:
    def __init__(self, transactions, prev_block_hash):
        self.transactions = transactions
        self.prev_block_hash = prev_block_hash
        self.merkle_root = self.calculate_merkle_root()
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_merkle_root(self):
        if len(self.transactions) == 1:
            return self.transactions[0].prev_transaction_hash
        else:
            merkle_tree = []
            for i in range(0, len(self.transactions), 2):
                if i + 1 < len(self.transactions):
                    merged = self.transactions[i].prev_transaction_hash + self.transactions[i + 1].prev_transaction_hash
                    merkle_tree.append(hashlib.sha256(merged.encode()).hexdigest())
                else:
                    merkle_tree.append(self.transactions[i].prev_transaction_hash)
            return self.calculate_merkle_root(merkle_tree)

    def calculate_hash(self):
        data = f"{self.merkle_root}{self.prev_block_hash}{self.nonce}".encode()
        return hashlib.sha256(data).hexdigest()

    def mine_block(self):
        while self.hash[:4] != "0" * 4:
            self.nonce += 1
            self.hash = self.calculate_hash()
