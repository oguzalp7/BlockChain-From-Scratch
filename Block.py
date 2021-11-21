import hashlib
import json
import datetime as dt


class Block:
    def __init__(self, index, proof, prev_hash):
        self.index = index
        self.timestamp = str(dt.datetime.now())
        self.data = {}
        self.previous_hash = prev_hash
        self.proof = proof

    def encode_block(self):
        dictionary = {"index": self.index, "timestamp": self.timestamp, "data": self.data, "proof": self.proof,
                      "previous_hash": self.previous_hash}
        encoded_block = json.dumps(dictionary, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest(), dictionary
