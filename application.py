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
Bank_balance = 100
pool=Pool()
# Create a genesis transaction
tx=Tx([], [[Bank.publickey,Bank_balance]], '0'*256)
transaction_hash = hashlib.sha256(str(tx).encode()).digest()
genesis_signature=Bank.privatekey.sign(transaction_hash)
prev_transaction_hash='0'*256
genesisins=[]
genesisouts=[]
genesis_transactions=[]
genesisouts.append([Bank.publickey,Bank_balance])
initial_transaction = Transaction(genesisins,genesisouts,Bank_balance,genesis_signature, prev_transaction_hash)
for i in range(1000):
    initial_transaction.amount+=10
    genesis_transactions.append(initial_transaction)



# Create a genesis block
genesis_block = Block(genesis_transactions, "0")
genesis_block.mine_block(users)
print(genesis_block)
# Create a blockchain with the genesis block
blockchain = Blockchain()
blockchain.chain.append(genesis_block)

blockchain.show_chain()
print(Bank.balance)
aakash=User()
print(aakash)
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

Bank.pay(aakash.publickey,1000,pool,blockchain,users)
print("payment 1 auccessful")
aakash.show_wallet()
Bank.pay(Adam.publickey,1000,pool,blockchain,users)
print("payment 2 auccessful")
Adam.show_wallet()
Bank.pay(Jason.publickey,1000,pool,blockchain,users)
print("payment 3 auccessful")
Jason.show_wallet()
Bank.pay(Robert.publickey,1000,pool,blockchain,users)
print("payment 4 auccessful")
Robert.show_wallet()
print(Bank)
Bank.pay(Chris.publickey,1000,pool,blockchain,users)
print("payment 5 auccessful")
Chris.show_wallet()
Bank.pay(Vicky.publickey,1000,pool,blockchain,users)
print("payment 6 auccessful")
Vicky.show_wallet()
aakash.pay(Jason.publickey,100,pool,blockchain,users)
print("payment 7 auccessful")
aakash.show_wallet()
Jason.show_wallet()
Adam.pay(Robert.publickey,100,pool,blockchain,users)
print("payment 8 auccessful")
Adam.show_wallet()
Robert.show_wallet()

Jason.pay(Vicky.publickey,100,pool,blockchain,users)
print("payment 9 auccessful")
Jason.show_wallet()
Vicky.show_wallet()

Robert.pay(Chris.publickey,100,pool,blockchain,users)
print("payment 10 auccessful")
Robert.show_wallet()
Chris.show_wallet()

Chris.pay(aakash.publickey,100,pool,blockchain,users)
print("payment 11 auccessful")
Chris.show_wallet()
aakash.show_wallet()

Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 12 auccessful")
Vicky.show_wallet()
Adam.show_wallet()

Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 13 auccessful")



print(aakash)
# Print the blockchain
blockchain.show_chain()
print("Bank Balance : " , Bank.balance,"Processing Balance : ",Bank.processing_balance,"change due : ",Bank.change)
print("Aakash Balance : " , aakash.balance,"Processing Balance : ",aakash.processing_balance,"change due : ",aakash.change)
print("Adam Balance : " , Adam.balance,"Processing Balance : ",Adam.processing_balance,"change due : ",Adam.change)
print("Jason Balance : " , Jason.balance,"Processing Balance : ",Jason.processing_balance,"change due : ",Jason.change)
print("Robert Balance : " , Robert.balance,"Processing Balance : ",Robert.processing_balance,"change due : ",Robert.change)
print("Chris Balance : " , Chris.balance,"Processing Balance : ",Chris.processing_balance,"change due : ",Chris.change)
print("Vicky Balance : " , Vicky.balance,"Processing Balance : ",Vicky.processing_balance,"change due : ",Vicky.change)
