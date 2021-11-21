import hashlib
import json
import datetime as dt
from flask import Flask, jsonify
from BlockChain import BlockChain


def main():
    blockchain = BlockChain()

    @app.route('/mine_block', methods=['GET'])
    def mine_block():
        previous_block = blockchain.get_previous_block()
        previous_proof = previous_block.proof
        proof = blockchain.proof_of_work(previous_proof)
        previous_hash = blockchain.hash(previous_block)
        block = blockchain.create_block(proof=proof, previous_hash=previous_hash)
        block.data["data"] = "random str"
        _, response = block.encode_block()
        return jsonify(response), 200


if __name__ == '__main__':
    app = Flask(__name__)
    main()
    app.run(host='localhost', port=5000)