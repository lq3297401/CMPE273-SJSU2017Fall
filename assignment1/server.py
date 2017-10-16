# curl http://localhost:8000/api/v1/scripts -d "data=It's my number" -X POST
# curl http://localhost:8000/api/v1/scripts/123456 -X GET

# curl http://localhost:8000/api/v1/scripts -d "data=@/$(pwd)/foo.py" -X POST

# curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts

import rocksdb

from flask import Flask, request
from flask_restful import Resource, Api
from random import *

app = Flask(__name__)
api = Api(app)

scripts = {}

class GlobalVar(Resource):
    # def __init__(self):
        db = rocksdb.DB("assignment1.db", rocksdb.Options(create_if_missing=True))

class ScriptUploader(Resource):
    def post(self):
        print("201 Created")
        x = randint(100000, 999999)    # Pick a random number between 100000 and 999999.
        s_id = str (x)
        scripts[s_id] = request.form['data']
        GlobalVar.db.put(s_id, scripts[s_id])
        return {s_id:GlobalVar.db.get(s_id)}
        # return {"script-id": s_id }

class ScriptDownloader(Resource):
    def get(self, script_id):
        print("get data from rocksDB")
        # return {script_id: scripts[script_id]}
        return GlobalVar.db.get(script_id)

api.add_resource(ScriptUploader, '/api/v1/scripts')
api.add_resource(ScriptDownloader, '/api/v1/scripts/<string:script_id>')

if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)
