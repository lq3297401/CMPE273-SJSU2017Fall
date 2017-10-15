# run "curl http://localhost:5000/19871216 -d "data=It's my birthday" -X PUT" in another terminal

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

scripts = {}

class ScriptUploader(Resource):
    def get(self, script_id):
        return {script_id: scripts[script_id]}

    def post(self, script_id):
        scripts[script_id] = request.form['data']
        return {script_id: scripts[script_id]}

api.add_resource(ScriptUploader, '/api/v1/scripts/<string:script_id>')

if __name__ == '__main__':
    app.run(port=8000)
    app.run(debug=True)
