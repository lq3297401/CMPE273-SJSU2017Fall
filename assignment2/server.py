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

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("database/assignment2.db", rocksdb.Options(create_if_missing=True))
        self.connectionCount = 0
        print("Server Ready!")

    def copyProcess(self, request, context):
        '''
        start server and client can start copy process
        '''
        selfId = self.connectionCount;
        arrDataDict.append([])
        self.connectionCount =  connectionCount + 1
        print("Start copy processing: " + str(selfId))

        while True:
            if len(arrDataDict[selfId]) != 0:
                data = arrDataDict[selfId].pop(0)
                yield datastore_pb2.ResponseAll(key=data["key"], value=data["value"])

    def followers:
        # need def followers

    @followers:
    def put(self, request, context):
        print("put")
        self.db.put(request.key, request.value)
        return datastore_pb2.GetRequest01(key=request.key, value=request.value)

    def get(self, request, context):
        print("get")
        # value = None
        value = self.db.get(request.key)
        return datastore_pb2.GetRequest01(key=request.key, value=request.value)

def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
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
