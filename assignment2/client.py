'''
################################## client.py #############################
#
################################## client.py #############################
'''
import grpc
import datastore_pb2
import argparse
import sys
import rocksdb

PORT = 3000

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
        print("Client start running...")

    def put(self, key, data):
        print("Pushing data to main database...")
        print("key = " + key + ", data = " + data)
        return self.stub.put(datastore_pb2.Request(key=key, data=data))

    def get(self, key):
        print("Geting data from main database...")
        return self.stub.get(datastore_pb2.Request(key=key))

if len(sys.argv) == 3:
    Key = sys.argv[1]
    Value = sys.argv[2]
    print(Key + ",***** " + Value)
elif len(sys.argv) == 2:
    Key = sys.argv[1]
    print(Key + "----- " )
else:
    print("Wrong Input. Please follow the input format as follows:\nExample for inserting key-value data: client.py key1 value1 \nExample for getting data from key1: client.py key1")
    exit()

client = DatastoreClient()
response = client.put(Key, Value)
print(response.key, response.data)
