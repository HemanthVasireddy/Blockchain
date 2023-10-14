import hashlib
import ecdsa
from Block import Block
from Transaction import Transaction
from Payment import Pay



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
