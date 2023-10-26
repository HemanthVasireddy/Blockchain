from Transaction import Transaction
import ecdsa
import hashlib

class Tx:
    def __init__(self,txins,txouts,amount):
        self.txins=txins
        self.txouts=txouts
        self.amount=amount


class User:
    def __init__(self, balance=0):
        self.privatekey=ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
        self.publickey=self.privatekey.get_verifying_key()
        self.wallet=[]
        self.balance=balance


    def addtowallet(self,transaction):
        self.wallet.append(transaction)
        self.balance+=transaction.amount
        return 'Successfully added funds to '+self.publickey


    def pay(self,recipient,amount):
        if amount>self.balance:
            return 'Insufficient funds'
        txins=[]
        target=0
        while target<amount:
            for transaction in self.wallet:
                target+=transaction.amount
                txins.append(transaction)
                self.wallet.remove(transaction)
        if target>amount:
            txouts=[[recipient,amount],[self.publickey,target-amount]]
        elif target==amount:
            txouts=[[recipient,amount]]
        tx=Tx(txins,txouts,target)
        previous_transaction_hash=hashlib.sha256(str(txins).encode()).digest()
        transaction_hash = hashlib.sha256(str(tx).encode()).digest()
        signature=self.privatekey.sign(transaction_hash)
        




        