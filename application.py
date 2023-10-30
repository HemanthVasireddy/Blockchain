import hashlib
from Block import Block
from User import User
from Transaction import Transaction
from Transaction import Tx
from Blockchain import Blockchain
import datetime
from Pool import Pool


users={}
user0 = User()
users[user0.publickey.to_string()]=user0
user0_balance = 10000000
# Create a transaction pool for the transactions to wait until the next block is mined
pool=Pool()
# Create a genesis transaction
tx=Tx([], [[user0.publickey,user0_balance]], '0'*256)
# Hashing the transaction data (transaction inputs, transaction outputs, Previous transaction hash, Amount)
transaction_hash = hashlib.sha256(str(tx).encode()).digest()
genesis_signature=user0.privatekey.sign(transaction_hash)
prev_transaction_hash='0'*256
genesisins=[]
genesisouts=[]
genesis_transactions=[]
genesisouts.append([user0.publickey,user0_balance])
print("Creating an intial transaction for genesis block")
print("================================================")
initial_transaction = Transaction(genesisins,genesisouts,user0_balance,genesis_signature, prev_transaction_hash)

print("Adding multiple transactions to genesis block")
print("=============================================")
for i in range(10):
    genesis_transactions.append(initial_transaction)



print("Creating a genesis block")
print("========================")
genesis_block = Block(genesis_transactions, "0")
print("Mining Genesis Block")
print("====================")
genesis_block.mine_block(users)
genesis_block.show_block()
print("Create a blockchain with the genesis block")
print("==========================================")
blockchain = Blockchain()
blockchain.chain.append(genesis_block)

print("Displaying the Blockchain") #( Output is large since there are 1000 transactions in the genesis block)
print("=========================")
blockchain.show_chain()
print("Printing the balance")
print("====================")
print(user0.balance)

print("Creating user object")
print("====================")
user1=User()
print(user1)
print("Adding user to the dictionary (Structure created in User.py file")
print("================================================================")
users[user1.publickey.to_string()]=user1
user2=User()
user3=User()
user4 = User()
user5 = User()
user6 = User()
users[user2.publickey.to_string()]=user2
users[user3.publickey.to_string()]=user3
users[user4.publickey.to_string()]=user4
users[user5.publickey.to_string()]=user5
users[user6.publickey.to_string()]=user6

print("Making transfers from user0 to all users")
print("The transfers won't be immediately reflected in the receipient's wallet as the block is not yet mined")
print("=====================================================================================================")
user0.pay(user1.publickey,1000,pool,blockchain,users)
print("payment 1 successful")
print("====================")
print("user1's wallet:")
user1.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()
user0.pay(user2.publickey,1000,pool,blockchain,users)
print("payment 2 successful")
print("====================")
print("user2's wallet:")
user2.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()
user0.pay(user3.publickey,1000,pool,blockchain,users)
print("payment 3 successful")
print("====================")
print("user3's's wallet:")
user3.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()
user0.pay(user4.publickey,1000,pool,blockchain,users)
print("payment 4 successful")
print("====================")
print("user4's wallet:")
user4.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()
print(user0)
user0.pay(user5.publickey,1000,pool,blockchain,users)
print("payment 5 successful")
print("====================")
print("user5's wallet")
user5.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()
user0.pay(user6.publickey,1000,pool,blockchain,users)
print("payment 6 successful")
print("====================")
print("user6's wallet")
user6.show_wallet()
print("user0's (Genesis) wallet:")
user0.show_wallet()

print("Transfers between users")
print("======================================")
user1.pay(user3.publickey,100,pool,blockchain,users)
print("payment 7 successful")
print("====================")
print("user1's wallet")
user1.show_wallet()
print("user3's wallet")
user3.show_wallet()
user2.pay(user4.publickey,100,pool,blockchain,users)
print("payment 8 successful")
print("====================")
print("user2's wallet")
user2.show_wallet()
print("user4's wallet")
user4.show_wallet()

user3.pay(user6.publickey,100,pool,blockchain,users)
print("payment 9 successful")
print("====================")
print("user3's wallet")
user3.show_wallet()
print("user6's wallet")
user6.show_wallet()

user4.pay(user5.publickey,100,pool,blockchain,users)
print("payment 10 successful")
print("=====================")
print("user4's wallet")
user4.show_wallet()
print("user5's wallet")
user5.show_wallet()

user5.pay(user1.publickey,100,pool,blockchain,users)
print("payment 11 successful")
print("=====================")
print("user5's wallet")
user5.show_wallet()
print("user1's wallet")
user1.show_wallet()

user6.pay(user2.publickey,100,pool,blockchain,users)
print("payment 12 successful")
print("=====================")
print("user6's wallet")
user6.show_wallet()
print("user2's wallet")
user2.show_wallet()

user6.pay(user2.publickey,100,pool,blockchain,users)
print("payment 13 successful")
print("=====================")

print(user1)
# Print the blockchain
print("Printing Blockchain")
blockchain.show_chain()

# Printing last block
print("Last Block")
print(blockchain.chain[-1].show_block())
print("Transactions in the Last Block")
print(blockchain.chain[-1].show_transactions())

print("user0 Balance : " , user0.balance,"Processing Balance : ",user0.processing_balance,"change due : ",user0.change)
print("user1 Balance : " , user1.balance,"Processing Balance : ",user1.processing_balance,"change due : ",user1.change)
print("user2 Balance : " , user2.balance,"Processing Balance : ",user2.processing_balance,"change due : ",user2.change)
print("user3 Balance : " , user3.balance,"Processing Balance : ",user3.processing_balance,"change due : ",user3.change)
print("user4 Balance : " , user4.balance,"Processing Balance : ",user4.processing_balance,"change due : ",user4.change)
print("user5 Balance : " , user5.balance,"Processing Balance : ",user5.processing_balance,"change due : ",user5.change)
print("user6 Balance : " , user6.balance,"Processing Balance : ",user6.processing_balance,"change due : ",user6.change)
