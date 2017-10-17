from flask import Flask, jsonify, abort, make_response, request
import os
import random
import json
import rocksdb

app = Flask(__name__)

@app.route('/api/v1/scripts/<script_id>', methods=['GET'])
def get_script(script_id):
    key = script_id
    result = db.get(key.encode())
    return result

@app.route('/api/v1/scripts', methods=['POST'])
def create_script():

    # myfile = open("foo.py")
    # str = myfile.read()
    # print(str)


    exec(open("foo.py").read())
    # key = '12345'
    # y = 'hello world'
    # db.put(key.encode(), y.encode())
    record = {
        # 'script-id': random.randint(10000, 99999),
        'script-id': 12345,
        'content': request.json['content']
    }
    return jsonify(record), 201

if __name__ == '__main__':
    # db = rocksdb.DB("hw1.db", rocksdb.Options(create_if_missing=True))
    app.run(port=8000 ,debug=True)
