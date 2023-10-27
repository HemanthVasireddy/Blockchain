import hashlib
import ecdsa
from Block import Block
from User import User
from Transaction import Transaction
from Transaction import Tx
from Blockchain import Blockchain


# Generate six pairs of public and private keys for users
Bank = User()
Bank_balance = 1000000

# Create a genesis transaction
tx=Tx([], [[Bank.publickey,Bank_balance]], '0'*256)
transaction_hash = hashlib.sha256(str(tx).encode()).digest()
genesis_signature=Bank.privatekey.sign(transaction_hash)
prev_transaction_hash='0'*256
genesisins=[]
genesisouts=[]
genesisouts.append([Bank.publickey,Bank_balance])
initial_transaction = Transaction(genesisins,genesisouts,Bank_balance,genesis_signature, prev_transaction_hash)
genesis_transactions=[]
genesis_transactions.append(initial_transaction)
genesis_transactions.append(initial_transaction)
# Create a genesis block
genesis_block = Block(genesis_transactions, "0")

# Create a blockchain with the genesis block
blockchain = Blockchain()
blockchain.addblock(genesis_block,0)



# Print the blockchain
for block in blockchain:
    print(f"Block Hash: {block.hash}")
    for transaction in block.transactions:
        print(f"\n  Transaction: Sender({transaction.sender}) \n -> Recipient({transaction.recipient}),\n Amount: {transaction.amount}")
