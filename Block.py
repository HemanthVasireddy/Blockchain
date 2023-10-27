
import hashlib
from typing import List
from Transaction import Transaction


# Define a simple Block class
class Block:
    def __init__(self, transactions:List[Transaction], prev_block_hash):
        self.transactions = transactions
        self.prev_block_hash = prev_block_hash
        self.merkle_root = self.calculate_merkle(transactions)
        self.nonce = 0
        self.hash = self.calculate_hash()

    '''def calculate_merkle_root(self,transactions):
        print(len(transactions),transactions[0])
        if len(transactions) == 1:
            for tx in transactions:
                print(tx,type(tx))
            return transactions[0].prev_transaction_hash
        else:
            merkle_tree = []
            for i in range(0, len(transactions), 2):
                if i + 1 < len(transactions):
                    merged = transactions[i].prev_transaction_hash + self.transactions[i + 1].prev_transaction_hash
                    merkle_tree.append(hashlib.sha256(merged.encode()).hexdigest())
                else:
                    merkle_tree.append(self.transactions[i].prev_transaction_hash)
            return self.calculate_merkle_root(merkle_tree)'''
    def merkle_root(tx_hashes):
        if len(tx_hashes) == 1:
            return tx_hashes[0]
        new_tx_hashes = []
        for i in range(0, len(tx_hashes), 2):
            left = tx_hashes[i]
            right = tx_hashes[i + 1] if i + 1 < len(tx_hashes) else left  # If the number of hashes is odd, duplicate the last one.
            combined = left + right
            new_tx_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
        return merkle_root(new_tx_hashes)

    def calculate_merkle(self,transactions):
        if not transactions:
            return None
        tx_hashes = [hashlib.sha256(str(transaction).encode()).hexdigest() for transaction in transactions]
        print(tx_hashes)
        return merkle_root(tx_hashes)

    def calculate_hash(self):
        data = f"{self.merkle_root}{self.prev_block_hash}{self.nonce}".encode()
        return hashlib.sha256(data).hexdigest()

    def mine_block(self):
        while self.hash[:4] != "0" * 4:
            self.nonce += 1
            self.hash = self.calculate_hash()
