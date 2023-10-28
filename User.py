import ecdsa
import hashlib
from Pool import Pool
from Transaction import Transaction
from Blockchain import Blockchain
from typing import List
import base64

class Tx:
    def __init__(self,txins,txouts,amount):
        self.txins=txins
        self.txouts=txouts
        self.amount=amount


class User:
    def __init__(self):
        self.privatekey=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.publickey=self.privatekey.get_verifying_key()
        self.wallet : List[Transaction]=[]
        self.pending : List[Transaction]=[]
        self.balance=0
        self.processing_balance=0
        self.change=0



    def pay(self,recipient,amount,pool:Pool,blockchain:Blockchain,users):
        if amount>self.balance:
            print('Insufficient funds in your account')
            return False
        txins=[]
        target=0
        print('Inside pay function')
        while target<amount:
            #print("Inside the first loop")
            for transaction in self.wallet:
                index=0
                for txout in transaction.txouts:
                    if txout[0]==self.publickey:
                        target+=txout[1]
                        txins.append([transaction,index])
                        self.pending.append(transaction)
                        self.wallet.remove(transaction)
                    index+=1
        print("Collected the required transactions from wallet....")
        if target>amount:
            txouts=[[recipient,amount],[self.publickey,target-amount]]
            self.change+=target-amount
            self.processing_balance+=target
            self.balance=self.balance-target
            print(txouts)
        elif target==amount:
            txouts=[[recipient,amount]]
            self.processing_balance+=target
            self.balance=self.balance-target

        tx=Tx(txins,txouts,target)
        previous_transaction_hash=hashlib.sha256(str(txins).encode()).digest()
        transaction_hash = hashlib.sha256(str(tx).encode()).digest()
        signature=self.privatekey.sign(transaction_hash)
        print("Adding transaction to the pool.....")
        pool.add_transaction(Transaction(txins,txouts,target, signature, previous_transaction_hash),blockchain,users)

    def show_wallet(self):
        print("---------------WALLET-----------------")
        for transaction in self.wallet:
            for txout in transaction.txouts:
                if txout[0]==self.publickey:
                    print(transaction.id() + "  " + str(txout[1]))
        print("Total available balance is : " + str(self.balance))
        print("Change that will be recieved after mining the next block : ",self.change)
        print("---------------PENDING WALLET-----------------")
        for transaction in self.pending:
            for txout in transaction.txouts:
                if txout[0]==self.publickey:
                    print(transaction.id() + "  " + str(txout[1]))
        print("Total Processing balance is : " + str(self.processing_balance))

            







        