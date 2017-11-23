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
registerInfo = {"default SlaveServer slaveId":"default SlaveServer port"}

PORT = 3000

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        os.system('rm server.db/LOCK')
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))
        self.slaveId = "0"
        self.port = str(PORT)
        print("-------- Main server start --------")

    def put(self, request, context):
        '''
        put data into RocksDB
        '''
        if(request.requestType=="data"):
            print("*** Put data into RocksDB ***")
            # print(request)
            print(request)
            self.db.put(request.key, request.data)
        elif(request.requestType=="register"):
            print("*** Put register info into Dictionary ***")
            print(request)
            registerInfo[request.key] = request.data
            for key, value in registerInfo.iteritems():
                print key, '\t', value

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
            # client = MyDatastoreServicer()
            # client.getInfo(client.request, client.context)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', PORT)
