'''
################################## server.py #############################
# Server Slave gRPC RocksDB Server
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import rocksdb
import sys
import os

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

MASTERSERVERPORT = 3000
PORT=6001

class MyDatastoreSlaveServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', MASTERSERVERPORT))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)

        #os.system('rm serverSlave.db/LOCK')
        os.system('rm serverSlave.db/LOCK')
        self.db = rocksdb.DB("serverSlave.db", rocksdb.Options(create_if_missing=True))
        self.slaveId = "0001"
        self.port = PORT
        self.put(self.slaveId, str(self.port))

        print("-------- Slave server start --------")
    def sync(self, request, context):
        '''
        put data into RocksDB
        '''
        if(request.requestType=="data"):
            print("*** Syncing! Put data into RocksDB ***")
            # print(request)
            print(request)
            self.db.put(request.key, request.data)
            print("*** Sync is done ***")
        return datastore_pb2.Response(key=request.key, data=request.data)

    def put(self, key, data, requestType="register"):
        print("*** Putting register info to main Dictionary ***")
        temmRequest = datastore_pb2.Request(key=key, data=data, requestType=requestType)
        print("Id = " + key + ", port = " + data)
        return self.stub.put(temmRequest)

    def get(self, request, context):
        '''
        get data from RocksDB
        '''
        print("*** Get data from RocksDB ***")
        print(request)
        value = self.db.get(request.key)
        print("value = ", value)
        return datastore_pb2.Response(key=request.key,data=value)


def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreSlaveServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    print("Server started at...%d" % port)
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    run('0.0.0.0', PORT)
