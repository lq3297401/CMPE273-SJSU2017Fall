'''
################################## client.py #############################
#
################################## client.py #############################
'''
import grpc
import datastore_pb2
import datastore_pb2_grpc
import argparse
import sys
import rocksdb
import os

PORT = 6001

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

        print("--------- Client start running ---------")

    def put(self, key, data, requestType="data"):
        print("*** Putting data to main database ***")
        print("key = " + key + ", data = " + data)
        self.requestType = "data"
        temmRequest = datastore_pb2.Request(key=key, data=data, requestType=requestType)
        return self.stub.put(temmRequest)

    def get(self, key):
        print("*** Geting data from main database ***")
        print("Search key = " + key)
        return self.stub.get(datastore_pb2.GetRequest(key=key))

    def delete(self, key, argu, requestType="delete"):
        print("*** Delete data from RocksDB ***")
        print("Delete key = " + key)
        temmRequest = datastore_pb2.DeleteRequest(key=key)
        return self.stub.delete(temmRequest)


if len(sys.argv) < 4:
    print("Not entough argunemnt, please follow the format below:\nFor inserting key-value data:\npython client.py <host> <port> <key1> <value1> \nFor getting data from slave server:\n python serverSlave.py <host> <port> <key1>")
    exit()

host = sys.argv[1]
port = int(sys.argv[2])
client = DatastoreClient(host, port)


if len(sys.argv) == 5:
    if sys.argv[4] == "delete":
        deleteKey = sys.argv[3]
        argu = sys.argv[4]
        client.delete(deleteKey,argu)

    else:
        insertKey = sys.argv[3]
        insertValue = sys.argv[4]
        client.put(insertKey,insertValue)


elif len(sys.argv) == 4:
    searchKey = sys.argv[3]
    response = client.get(searchKey)
    print(response)
else:
    print("Wrong argunemnt, please follow the format below:\nFor inserting key-value data: client.py <host> <port> <key1> <value1> \nFor getting data from slave server: python serverSlave.py <host> <port> <key1>")
    exit()
