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

PORT = 3000

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)

        DatabaseName = "server.db"
        os.system('rm server.db/LOCK')
        # DatabaseName = "db/follower_" + FollowerId + ".db"
        self.db = rocksdb.DB(DatabaseName,rocksdb.Options(create_if_missing=True))

        print("--------- Client start running ---------")

    # def sendInfo(self, slaveId, port):
    #     print("Sending slaveServer slaveId and port to main server")
    #     # rpc sendInfo(SlaveRegisterRequest) returns (SlaveRegisterResponse) {}
    #     infoResponse=self.SlaveRegisterRequest(slaveId=1 port=3000)
    #     return datastore_pb2_grpc.SlaveRegisterResponse()


    def put(self, key, data):
    # def put(self, data):
        print("*** Putting data to main database ***")
        print("key = " + key + ", data = " + data)
        temmRequest = datastore_pb2.Request(key=key, data=data)
        # print("temReq = ", temReq)
        return self.stub.put(temmRequest)

    def get(self, key):
        print("*** Geting data from main database ***")
        print("Search key = " + key)
        value = self.db.get(key)
        print(key, value)
        return self.stub.get(datastore_pb2.GetRequest(key=key))

client = DatastoreClient()

if len(sys.argv) == 3:
    insertKey = sys.argv[1]
    insertValue = sys.argv[2]
    client.put(insertKey,insertValue)

elif len(sys.argv) == 2:
    searchKey = sys.argv[1]
    client.get(searchKey)
else:
    print("Wrong Input. Please follow the input format as follows:\nExample for inserting key-value data: client.py key1 value1 \nExample for getting data from key1: client.py key1")
    exit()
