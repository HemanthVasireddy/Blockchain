import hashlib
from Block import Block
from User import User
from Transaction import Transaction
from Transaction import Tx
from Blockchain import Blockchain
import datetime
from Pool import Pool

# Generate six pairs of public and private keys for users
users={}
Bank = User()
users[Bank.publickey.to_string()]=Bank
Bank_balance = 10000000
# Create a transaction pool for the transactions to wait until the next block is mined
pool=Pool()
# Create a genesis transaction
tx=Tx([], [[Bank.publickey,Bank_balance]], '0'*256)
# Hashing the transaction data (transaction inputs, transaction outputs, Previous transaction hash, Amount)
transaction_hash = hashlib.sha256(str(tx).encode()).digest()
# Creating digital signature using private key
genesis_signature=Bank.privatekey.sign(transaction_hash)
prev_transaction_hash='0'*256
genesisins=[]
genesisouts=[]
genesis_transactions=[]
genesisouts.append([Bank.publickey,Bank_balance])
# Creating an intial transaction for genesis block
initial_transaction = Transaction(genesisins,genesisouts,Bank_balance,genesis_signature, prev_transaction_hash)

# Adding multiple transactions to genesis block
for i in range(10):
    initial_transaction.amount+=10
    genesis_transactions.append(initial_transaction)



# Create a genesis block
genesis_block = Block(genesis_transactions, "0")
genesis_block.mine_block(users)
genesis_block.show_block()
# Create a blockchain with the genesis block
blockchain = Blockchain()
blockchain.chain.append(genesis_block)

# Displaying the Blockchain ( Output is large since there are 1000 transactions in the genesis block)
blockchain.show_chain()
# Printing the balance
print(Bank.balance)

# Creating user object
aakash=User()
print(aakash)
# Adding user to the dictionary (Structure created in User.py file)
users[aakash.publickey.to_string()]=aakash
Adam=User()
Jason=User()
Robert = User()
Chris = User()
Vicky = User()
users[Adam.publickey.to_string()]=Adam
users[Jason.publickey.to_string()]=Jason
users[Robert.publickey.to_string()]=Robert
users[Chris.publickey.to_string()]=Chris
users[Vicky.publickey.to_string()]=Vicky

# Making transfers from Bank to all users
Bank.pay(aakash.publickey,1000,pool,blockchain,users)
print("payment 1 auccessful")
print("aakash's wallet")
aakash.show_wallet()
Bank.pay(Adam.publickey,1000,pool,blockchain,users)
print("payment 2 auccessful")
print("Adam's wallet")
Adam.show_wallet()
Bank.pay(Jason.publickey,1000,pool,blockchain,users)
print("payment 3 auccessful")
print("Jason's's wallet")
Jason.show_wallet()
Bank.pay(Robert.publickey,1000,pool,blockchain,users)
print("payment 4 auccessful")
print("Robert's wallet")
Robert.show_wallet()
print(Bank)
Bank.pay(Chris.publickey,1000,pool,blockchain,users)
print("payment 5 auccessful")
print("Chris's wallet")
Chris.show_wallet()
Bank.pay(Vicky.publickey,1000,pool,blockchain,users)
print("payment 6 auccessful")
print("Vicky's wallet")
Vicky.show_wallet()

# Transfers between users
aakash.pay(Jason.publickey,100,pool,blockchain,users)
print("payment 7 auccessful")
print("aakash's wallet")
aakash.show_wallet()
print("Jason's wallet")
Jason.show_wallet()
Adam.pay(Robert.publickey,100,pool,blockchain,users)
print("payment 8 auccessful")
print("Adam's wallet")
Adam.show_wallet()
print("Robert's wallet")
Robert.show_wallet()

Jason.pay(Vicky.publickey,100,pool,blockchain,users)
print("payment 9 auccessful")
print("Jason's wallet")
Jason.show_wallet()
print("Vicky's wallet")
Vicky.show_wallet()

Robert.pay(Chris.publickey,100,pool,blockchain,users)
print("payment 10 auccessful")
print("Robert's wallet")
Robert.show_wallet()
print("Chris's wallet")
Chris.show_wallet()

Chris.pay(aakash.publickey,100,pool,blockchain,users)
print("payment 11 auccessful")
print("Chris's wallet")
Chris.show_wallet()
print("aakash's wallet")
aakash.show_wallet()

Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 12 auccessful")
print("Vicky's wallet")
Vicky.show_wallet()
print("Adam's wallet")
Adam.show_wallet()

Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 13 auccessful")

print(aakash)
# Print the blockchain
print("Printing Blockchain")
blockchain.show_chain()

# Printing last block
print("Last Block")
print(blockchain.chain[-1].show_block())
print("Transactions in the Last Block")
print(blockchain.chain[-1].show_transactions())

print("Bank Balance : " , Bank.balance,"Processing Balance : ",Bank.processing_balance,"change due : ",Bank.change)
print("Aakash Balance : " , aakash.balance,"Processing Balance : ",aakash.processing_balance,"change due : ",aakash.change)
print("Adam Balance : " , Adam.balance,"Processing Balance : ",Adam.processing_balance,"change due : ",Adam.change)
print("Jason Balance : " , Jason.balance,"Processing Balance : ",Jason.processing_balance,"change due : ",Jason.change)
print("Robert Balance : " , Robert.balance,"Processing Balance : ",Robert.processing_balance,"change due : ",Robert.change)
print("Chris Balance : " , Chris.balance,"Processing Balance : ",Chris.processing_balance,"change due : ",Chris.change)
print("Vicky Balance : " , Vicky.balance,"Processing Balance : ",Vicky.processing_balance,"change due : ",Vicky.change)
