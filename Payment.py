import hashlib
import ecdsa
from Block import Block
from Transaction import Transaction

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

class Pay:

    def add_transaction(sender, recipient, amount, ):
        new_transaction = Transaction(sender.verifying_key.to_string().hex(), recipient.verifying_key.to_string().hex(), amount)
        new_transaction.sign_transaction(sender.to_string().hex())

        last_block = blockchain[-1]
        if len(last_block.transactions) < 4:
            last_block.transactions.append(new_transaction)
        else:
            new_block = Block([new_transaction], last_block.hash)
            new_block.mine_block(2)  # Adjust the difficulty as needed
            blockchain.append(new_block)
    