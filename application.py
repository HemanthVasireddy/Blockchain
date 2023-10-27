import hashlib
from Block import Block
from User import User
from Transaction import Transaction
from Transaction import Tx
from Blockchain import Blockchain
import base64
from Pool import Pool

# Generate six pairs of public and private keys for users
users={}
Bank = User()
users[Bank.publickey.to_string()]=Bank
Bank_balance = 1000
pool=Pool()
# Create a genesis transaction
tx=Tx([], [[Bank.publickey,Bank_balance]], '0'*256)
transaction_hash = hashlib.sha256(str(tx).encode()).digest()
genesis_signature=Bank.privatekey.sign(transaction_hash)
prev_transaction_hash='0'*256
genesisins=[]
genesisouts=[]
genesisouts.append([Bank.publickey,Bank_balance])
initial_transaction = Transaction(genesisins,genesisouts,Bank_balance,genesis_signature, prev_transaction_hash)
for i in range(1000):
    Bank.wallet.append(initial_transaction)
    Bank.balance+=initial_transaction.amount

genesis_transactions=[]
genesis_transactions.append(initial_transaction)
genesis_transactions.append(initial_transaction)
# Create a genesis block
genesis_block = Block(genesis_transactions, "0")
print(genesis_block)
# Create a blockchain with the genesis block
blockchain = Blockchain()
blockchain.addblock(genesis_block,users)

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
Bank.pay(Adam.publickey,1000,pool,blockchain,users)
print("payment 2 auccessful")
Bank.pay(Jason.publickey,1000,pool,blockchain,users)
print("payment 3 auccessful")
Bank.pay(Robert.publickey,1000,pool,blockchain,users)
print("payment 4 auccessful")
Bank.pay(Chris.publickey,1000,pool,blockchain,users)
print("payment 5 auccessful")
Bank.pay(Vicky.publickey,1000,pool,blockchain,users)
print("payment 6 auccessful")
aakash.pay(Jason.publickey,100,pool,blockchain,users)
print("payment 7 auccessful")
Adam.pay(Robert.publickey,100,pool,blockchain,users)
print("payment 8 auccessful")
Jason.pay(Vicky.publickey,100,pool,blockchain,users)
print("payment 9 auccessful")
Robert.pay(Chris.publickey,100,pool,blockchain,users)
print("payment 10 auccessful")
Chris.pay(aakash.publickey,100,pool,blockchain,users)
print("payment 11 auccessful")
Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 12 auccessful")
Vicky.pay(Adam.publickey,100,pool,blockchain,users)
print("payment 13 auccessful")



print(aakash)
# Print the blockchain
blockchain.show_chain()
print("Bank Balance : " + Bank.balance)
print("Aakash Balance : " + aakash.balance)
print("Adam Balance : " + Adam.balance)
print("Jason Balance : " + Jason.balance)
print("Robert Balance : " + Robert.balance)
print("Chris Balance : " + Chris.balance)
print("Vicky Balance : " + Vicky.balance)
