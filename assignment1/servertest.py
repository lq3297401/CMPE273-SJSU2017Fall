# reference: http://flask.pocoo.org/docs/0.12/patterns/fileuploads/
#            http://pythonexample.com/code/flask-file-upload-example/
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from random import *
json

UPLOAD_FOLDER = '/Users/qi/Desktop/273Git/assignment1/upload/'  #the place that file save
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'py', 'gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/api/v1/scripts', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'data' not in request.files:  # the request use "data" to passing file address
            print 'no file'
            return redirect(request.url)
        file = request.files['data']  # the request use "data" to passing file address
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            print 'no filename'
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            # return redirect(url_for('uploaded_file',filename=filename))

    return '201 Created\n'
    # return os.path.join(app.config['UPLOAD_FOLDER'], filename)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)


if __name__ == "__main__":
    app.run(port=8000)
    app.run(debug=True)
