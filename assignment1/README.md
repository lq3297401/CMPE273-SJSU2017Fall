Self note:

1. Install Flask-RESTful with pip(Flask-RESTful requires Python version 2.6, 2.7, 3.3, or 3.4.):
    pip install flask-restful

2. Install rocksDB, python-rocksdb:
  brew install rocksdb
  sudo pip install python-rocksdb

3. Run server in 1st terminal:
    python server.py

4. Run "curl request" in 2nd terminal:
    curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@/$(pwd)/foo.py" http://localhost:8000/api/v1/scripts
    //this request will generate a random number as script_id

    curl -i http://localhost:8000/api/v1/scripts/<script_id>
    // replace the <script_id> as the one in output above
