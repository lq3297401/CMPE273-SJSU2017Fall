'''
################################## client.py #############################
# Client.py
################################## client.py #############################
'''
import random, string
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import argparse
import uuid
import rocksdb
from time import sleep
from itertools import repeat

PORT = 3000

'''
Request Generator
'''

def randString(length=8):
    valid_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    return ''.join((random.choice(valid_letters) for i in range(length)))

def randomNumber():
    x = str(random.randint(0, 100))
    return x

def generateData(key, data):
    return datastore_pb2.Request(key=key,data=data)

def generateTestCases():
    testCases = [
        generateData(randomNumber(), randString()),
        generateData(randomNumber(), randString()),
        generateData(randomNumber(), randString()),
        generateData("testKey1", "testValue1"),
        generateData("testKey2", "testValue2"),
    ]
    for task in testCases:
        print("Sending request key = " + task.key + ", data = " + task.data)
        yield task

class DatastoreClient():

    def __init__(self, host='0.0.0.0', port=PORT):
        self.channel = grpc.insecure_channel('%s:%d' % (host, port))
        self.stub = datastore_pb2.DatastoreStub(self.channel)
        self.db = rocksdb.DB("slaveServer.db", rocksdb.Options(create_if_missing=True))

    '''
    streaming data function of main server
    '''

    def put(self):
        dataRequests = self.stub.put(generateTestCases())
        for dataRequest in dataRequests:
            print("Inserting data to Main server that key = " + dataRequest.key + ", value = " + dataRequest.data)

    def get(self):
        dataRequests = self.stub.get(generateTestCases())
        if dataRequests == None:
            print("Didn't find the data for getting that key = " + dataRequest.key)
        else:
            for dataRequest in dataRequests:
                data=self.db.get(dataRequest.key.encode())
                print("Getting data from Main server that key = " + dataRequest.key  + ", value = " + str(data))

    def delete(self):
        dataRequests = self.stub.delete(generateTestCases())
        if dataRequests == None:
            print("Didn't find the data for deleting that key = " + dataRequest.key)
        else:
            for dataRequest in dataRequests:
                print("Deleting data from Main server that key = " + dataRequest.key + ", value = " + dataRequest.data)

    '''
    streaming data main server send to slave server
    '''

    def replicator(self, requestInfo):
        dataRequest = self.stub.replicator(datastore_pb2.PullRequest(requestInfo=requestInfo))

        if requestInfo == 'put':
            for requestInfo in dataRequest:
                self.db.put(requestInfo.key.encode(), requestInfo.data.encode())
                if requestInfo.data == self.db.get(requestInfo.key.encode()).decode():
                    print("Inserting data to Slave server that key = " + requestInfo.key + ", value = " + requestInfo.data)

        elif requestInfo == 'get':
            for requestInfo in dataRequest:
                getValue = self.db.get(requestInfo.key.encode())
                if getValue == None:
                    print("Didn't find data for geting that key = " + requestInfo.key)
                else:
                    print("Getting data that key = " + str(requestInfo.key) + ", value = " + str(getValue))

        elif requestInfo == 'delete':
            for requestInfo in dataRequest:
                getValue = self.db.get(requestInfo.key.encode())
                if getValue == None:
                    print("Didn't find data for deleting that key = " + requestInfo.key)
                else:
                    self.db.delete(requestInfo.key.encode())
                    print("Deleting data that key = " + str(requestInfo.key) + ", value = " + str(getValue))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("host", help="for testing")
    args = parser.parse_args()
    print("Client is connecting to Server at {}:{}...".format(args.host, PORT))
    client = DatastoreClient(host=args.host)

    '''
    Test Cases
    '''
    print("--------------- 1-1. Inserting data to Main server ----------------")
    client.put()
    print("**-------- Finishing inserting data to Main server --------**\n")
    sleep(1)

    print("--------------- 1-2. Replicating inserting to Slave server ----------------")
    client.replicator("put")
    print("**-------- Finishing inserting data to Slave server --------**\n")
    sleep(1)

    print("--------------- 2-1. Getting data to Main server ----------------")
    client.get()
    print("**-------- Finishing getting data from Main server --------**\n")
    sleep(1)

    print("--------------- 2-2. Replicating getting to Slave server ----------------")
    client.replicator("get")
    print("**-------- Finishing getting data from Slave server --------**\n")
    sleep(1)

    print("--------------- 3-1. Deleting data from Main server ----------------")
    client.delete()
    print("**-------- Finishing inserting data to Main server --------**\n")
    sleep(1)

    print("--------------- 3-2. Replicating deleting to Slave server ----------------")
    client.replicator("delete")
    print("**-------- Finishing deleting data to Slave server --------**\n")
    sleep(1)

if __name__ == "__main__":
    main()
