# curl http://localhost:8000/api/v1/scripts -d "data=It's my birthday" -X POST
# curl http://localhost:8000/api/v1/scripts/123456 -X GET

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

scripts = {}

class ScriptUploader(Resource):
    def post(self):
        s_id="123456"
        scripts[s_id] = request.form['data']
        return {"scripts": s_id}

class ScriptDownloader(Resource):
    def get(self, script_id):
        return {script_id: scripts[script_id]}

api.add_resource(ScriptUploader, '/api/v1/scripts')
api.add_resource(ScriptDownloader, '/api/v1/scripts/<string:script_id>')

if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)
