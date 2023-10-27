from typing import Dict
import hashlib
from typing import List
from Transaction import Transaction
import ecdsa
from datetime import datetime


class User:
    def __init__(self):
        self.privatekey=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.publickey=self.privatekey.get_verifying_key()
        self.wallet=[]
        self.balance=0


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
        print('--------------------------------------------------')
        return self.merkle_root(tx_hashes)

    def calculate_hash(self):
        data = f"{self.merkle_root}{self.prev_block_hash}{self.nonce}".encode()
        return hashlib.sha256(data).hexdigest()
    
    def mine_block(self,users:Dict[str,User]):
        while self.hash[:4] != "0" * 4:
            self.nonce += 1
            self.hash = self.calculate_hash()
        self.mine_time=datetime.now()
        for transaction in self.transactions:
            for txout in transaction.txouts:
                users[txout[0].to_string()].balance+=txout[1]
                users[txout[0].to_string()].wallet.append(transaction)

class Blockchain:
    def __init__(self):
        self.chain=[]

    def addblock(self,block:Block,users:Dict[str,User]):
        block.mine_block(users)
        self.chain.append(block)

    def show_chain(self):
        for block in self.chain:
            print(f"Block Hash: {block.hash}")
            for transaction in block.transactions:
                print(transaction.get_transaction_data())



