1. Install Flask-RESTful with pip(Flask-RESTful requires Python version 2.6, 2.7, 3.3, or 3.4.):
    pip install flask-restful
2. Run server in 1st terminal:
    python server.py
3. Run "curl request" in 2nd terminal:
    curl -i -X POST -H "Content-Type: multipart/form-data" -F "data=@/tmp/foo.py" http://localhost:8000/api/v1/scripts
