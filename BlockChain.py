import hashlib
from Block import Block

class BlockChain(object):
    def __init__(self):
        self.chain = []
        self.genesis_block = self.create_block(proof=1, previous_hash="0")

    def create_block(self, proof, previous_hash):
        block = Block(index=len(self.chain) + 1, proof=proof, prev_hash=previous_hash)
        self.chain.append(block)
        return block

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while not check_proof:
            hash_operation = hashlib.sha256(str(new_proof ** 2 - previous_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        return block.encode_block()

    def is_chain_valid(self, chain):
        if len(chain) == 0:
            return False
        prev_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block.previous_hash != self.hash(prev_block):
                return False
            prev_proof = prev_block.proof
            proof = block.proof
            hash_operation = hashlib.sha256(str(proof ** 2 - prev_proof ** 2).encode()).hexdigest()
            if hash_operation[:4] != "0000":
                return False
            previous_block = block
            block_index += 1
        return True