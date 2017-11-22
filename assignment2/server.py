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

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24
registerInfo = {
            "default SlaveServer slaveId":"default SlaveServer port"
}

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))
        print("-------- Main server start --------")


    def put(self, request, context):
        '''
        put data into RocksDB
        '''
        print("*** Put data into RocksDB ***")
        # print(request)
        print(request)

        # self.db.put(request.key.encode(), request.data.encode())
        self.db.put(request.key, request.data)
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



# value = None
# value = self.db.get(request.data.encode())
# return datastore_pb2.Response(data=value)


    # def register(self, request, context):
    #     '''
    #     get slave register information
    #     '''
    #     print("-------- Slave server information --------")
    #
    #     registerInfo[request.slaveId] = request.port
    #     # dict = {'SlaveServer slaveId': request.slaveId, 'SlaveServer port': request.port}
    #     # print "SlaveServer slaveId: ", dict['SlaveServer slaveId'], "SlaveServer port: ", dict[request.port]
    #
    #     # slaveId = self.db.put(request.slaveId, request.port)
    #     # print("Register slaveId = " + request.slaveId + ", register port = " + request.port)
    #     return datastore_pb2.SlaveRegisterResponse(slaveId=request.slaveId, port=request.port)

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
