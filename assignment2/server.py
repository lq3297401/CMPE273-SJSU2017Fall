'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server
################################## server.py #############################
'''
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb
import sys

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))
        print("-------- Main server start --------")

    def put(self, request, context):
        '''
        put data into RocksDB
        '''
        print("-------- Put data into RocksDB --------")
        print(request)

        self.db.put(request.key, request.data)
        return datastore_pb2.Response(key=request.key, data=request.data)

    def get(self, request, context):
        '''
        get data from RocksDB
        '''
        print("-------- Get data from RocksDB --------")
        value = self.db.get(request.key)
        return datastore_pb2.Response(key=request.key, data=value)

    def register(self, request, context):
        '''
        get slave register information
        '''
        print("-------- Slave server information --------")
        id = self.db.put(request.id, request.port)
        print("Register id = " + request.id + ", register port = " + request.port)
        return datastore_pb2.SlaveRegisterResponse(id=request.id, port=request.port)

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
    run('0.0.0.0', 3000)
