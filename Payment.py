import hashlib
import ecdsa
from Block import Block
from Transaction import Transaction

class Pay:

    def add_transaction(sender, recipient, amount):
        new_transaction = Transaction(sender.verifying_key.to_string().hex(), recipient.verifying_key.to_string().hex(), amount)
        new_transaction.sign_transaction(sender.to_string().hex())

        last_block = blockchain[-1]
        if len(last_block.transactions) < 4:
            last_block.transactions.append(new_transaction)
        else:
            new_block = Block([new_transaction], last_block.hash)
            new_block.mine_block(2)  # Adjust the difficulty as needed
            blockchain.append(new_block)
    