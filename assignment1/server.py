# curl http://localhost:8000/api/v1/scripts -d "data=It's my number" -X POST
# curl http://localhost:8000/api/v1/scripts/123456 -X GET

# curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts

import rocksdb

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

scripts = {}

class ScriptUploader(Resource):
    def __init__(self):
        self.db = rocksdb.DB("assignment1.db", rocksdb.Options(create_if_missing=True))

    def post(self):
        print("put data in rocksDB")
        s_id="123456"
        scripts[s_id] = request.form['data']
        self.db.put(s_id, scripts[s_id])
        return self.db.get(s_id)
        # return {"script-id": s_id }

class ScriptDownloader(Resource):
    def get(self, script_id):
        return {script_id: scripts[script_id]}

api.add_resource(ScriptUploader, '/api/v1/scripts')
api.add_resource(ScriptDownloader, '/api/v1/scripts/<string:script_id>')

if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)
