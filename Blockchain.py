from Block import Block

class Blockchain:
    def __init__(self):
        self.chain=[]

    def addblock(self,transactions,prevblockhash):
        block = Block(transactions,prevblockhash)
        block.mine_block()
        self.chain.append(block)


