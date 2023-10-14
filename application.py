import hashlib
import ecdsa
from Block import Block
from Transaction import Transaction
from Payment import Pay

# Generate six pairs of public and private keys for users
keys = [ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1) for _ in range(6)]

# Initial user with 100 coins
genesis_user = keys[0]
genesis_user_balance = 100

# Create a genesis transaction
genesis_transaction = Transaction(genesis_user.verifying_key.to_string().hex(), keys[0].verifying_key.to_string().hex(), genesis_user_balance)
genesis_transaction.sign_transaction(genesis_user.to_string().hex())

# Create a genesis block
genesis_block = Block([genesis_transaction], "0")

# Create a blockchain with the genesis block
blockchain = [genesis_block]

# Add more blocks with transactions


# Perform transactions between keys
pay.add_transaction(keys[1], keys[2], 10)
pay.add_transaction(keys[2], keys[3], 5)
pay.add_transaction(keys[1], keys[4], 8)
pay.add_transaction(keys[4], keys[5], 3)

# Verify transactions
for block in blockchain:
    for transaction in block.transactions:
        if transaction.is_valid():
            print(f"Transaction in block {block.hash} is valid.")
        else:
            print(f"Invalid transaction in block {block.hash}.")

# Print the blockchain
for block in blockchain:
    print(f"Block Hash: {block.hash}")
    for transaction in block.transactions:
        print(f"\n  Transaction: Sender({transaction.sender}) \n -> Recipient({transaction.recipient}),\n Amount: {transaction.amount}")
