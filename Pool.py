from Transaction import Transaction
from Blockchain import Blockchain
import hashlib
from typing import List

class Block:
    def __init__(self, transactions:List[Transaction], prev_block_hash):
        self.transactions = transactions
        self.prev_block_hash = prev_block_hash
        self.merkle_root = self.calculate_merkle(transactions)
        print(self.merkle_root)
        self.nonce = 0
        self.hash = self.calculate_hash()
        self.mine_time = None
    
    def merkle_root(self,tx_hashes):
        print("Inside merkle_root function")
        if len(tx_hashes) == 1:
            print(tx_hashes[0])
            return tx_hashes[0]
        new_tx_hashes = []
        for i in range(0, len(tx_hashes), 2):
            left = tx_hashes[i]
            right = tx_hashes[i + 1] if i + 1 < len(tx_hashes) else left  # If the number of hashes is odd, duplicate the last one.
            combined = left + right
            new_tx_hashes.append(hashlib.sha256(combined.encode()).hexdigest())
        return self.merkle_root(new_tx_hashes)

    def calculate_merkle(self,transactions):
        if not transactions:
            return None
        tx_hashes = [hashlib.sha256(str(transaction).encode()).hexdigest() for transaction in transactions]
        print(tx_hashes)
        return self.merkle_root(tx_hashes)

    def calculate_hash(self):
        data = f"{self.merkle_root}{self.prev_block_hash}{self.nonce}".encode()
        return hashlib.sha256(data).hexdigest()

class Pool:
    def __init__(self):
        self.transactions=[]

    def add_transaction(self,transaction:Transaction,blockchain:Blockchain,users):
        if len(self.transactions)<4:
            self.transactions.append(transaction)
        else:
            blockchain.addblock(Block(self.transactions,blockchain.chain[-1].hash),users)
            self.transactions=[]
            self.transactions.append(transaction)
        print("Added Transaction to the pool")
