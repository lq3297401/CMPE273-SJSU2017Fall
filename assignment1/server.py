# reference: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
#            http://pythonexample.com/code/flask-file-upload-example/
import os
from os import path
from flask import Flask, request, redirect, url_for, send_from_directory, jsonify
from werkzeug.utils import secure_filename
from random import *
import rocksdb
import sys
import StringIO
import contextlib


UPLOAD_FOLDER = '/Users/qi/Desktop/273Git/assignment1/upload/'  #the place that file save
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'py', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/v1/scripts', methods=['POST'])
def upload_file():
    x = randint(100000, 999999)    # Pick a random number between 100000 and 999999 as s_id.
    s_id = str (x)
    if request.method == 'POST':
        # check if the post request has the file part
        if 'data' not in request.files:  # the request use "data" to passing file address
            print 'no file'
            return redirect(request.url)
        file = request.files['data']  # the request use "data" to passing file address
        # if user does not select file, browser also submit a empty part without filename
        if file.filename == '':
            print 'no filename'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            file_address = str(os.path.join(app.config['UPLOAD_FOLDER'], filename)) #/Users/qi/Desktop/273Git/assignment1/upload/foo.py
            db.put(s_id, file_address)
            result = {'script-id':s_id}
            print '201 Created\n'
            return jsonify(result)


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)

@contextlib.contextmanager
def stdoutIO(stdout=None):
    old = sys.stdout
    if stdout is None:
        stdout = StringIO.StringIO()
    sys.stdout = stdout
    yield stdout
    sys.stdout = old


@app.route('/api/v1/scripts/<script_id>', methods=['GET'])
def get_script(script_id):
    fileDir = db.get(script_id)
    print '200 OK'
    with stdoutIO() as s:
        exec(open(fileDir).read())
    return s.getvalue()


if __name__ == "__main__":
    db = rocksdb.DB("assignment1.db", rocksdb.Options(create_if_missing=True))
    app.run(port=8000)
    app.run(debug=True)
