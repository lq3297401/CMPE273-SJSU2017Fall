'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
# import uuslaveId
import rocksdb
import sys
import os

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
registerInfo = {}

PORT = 3000

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        os.system('rm server.db/LOCK')
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))
        # self.slaveId = "0"
        self.port = str(PORT)
        # print("registerInfo begin")
        for key in registerInfo:
            print "the key name is" + key + "and its value is" + registerInfo[key]
        print("-------- Main server start --------")

    def sync(self, key, data, requestType):
        # def put(self, data):
        if requestType=="data":
            print("*** Putting data to slave database ***")
            print("key = " + key + ", data = " + data)
            temmRequest = datastore_pb2.SyncRequest(key=key, data=data, requestType=requestType)
            for key, value in registerInfo.iteritems():
                print("Pushing data to the slave server Id = " + key)
                port = int(value)
                channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', port))
                self.stub = datastore_pb2.DatastoreStub(channel)
                print("temmRequest:",temmRequest)
                return self.stub.sync(temmRequest)

        elif requestType=="delete":
            print("*** Deleteing data from database ***")
            print("Delete key = " + key)
            temmRequest = datastore_pb2.SyncRequest(key=key, data=data, requestType=requestType)
            for key, value in registerInfo.iteritems():
                print("Deleteing data from the slave server Id = " + key)
                port = int(value)
                channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', port))
                self.stub = datastore_pb2.DatastoreStub(channel)
                print("temmRequest:",temmRequest)
                return self.stub.sync(temmRequest)


    def put(self, request, context):
        '''
        put data into RocksDB/dictionary
        '''
        if request.requestType=="data":
            print("*** Put data into RocksDB ***")
            print("key = " + request.key + ", data = " + request.data)
            print(request)
            self.db.put(request.key, request.data)
            self.sync(request.key, request.data, request.requestType)
            return datastore_pb2.Response(key=request.key, data=request.data)

        elif request.requestType=="register":
            print("*** Saving slave server data to dictionary ***")
            print(request)
            registerInfo[request.key] =  request.data
            return datastore_pb2.Response(key=request.key, data=request.data)


    def get(self, request, context):
        '''
        get data from RocksDB
        '''
        print("*** Get data from RocksDB ***")
        print(request)
        value = self.db.get(request.key)
        print("value = ", value)
        return datastore_pb2.Response(key=request.key,data=value)

    def delete(self, request, context):
        '''
        delete data from RocksDB
        '''
        print("*** Delete data from RocksDB ***")
        print(request)
        self.db.delete(request.key)
        value = self.db.get(request.key)
        print("Delete key: ", request.key, "Delete value: ", value)
        deleteMsg = "Delete successfully"
        requestType="delete"
        self.sync(request.key, value, requestType)
        return datastore_pb2.DeleteMsg(deleteMsg=deleteMsg, key=request.key)

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run('0.0.0.0', PORT)
