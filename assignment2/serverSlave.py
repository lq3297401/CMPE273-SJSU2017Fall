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
# registerInfo = {
#             "default SlaveServer slaveId":"default SlaveServer port"
# }

PORT = 3001
# class MyDatastoreSlaveServicer():
class MyDatastoreSlaveServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', PORT))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)

        # os.system('rm serverSlave.db/LOCK')
        # self.db = rocksdb.DB("serverSlave.db", rocksdb.Options(create_if_missing=True))
        self.slaveId = "1"
        self.port = PORT

        print("-------- Slave server start --------")

    def put(self, key, data, requestType="register"):
        print("*** Putting register info to main main server dictionary ***")
        print("Id = " + key + ", port = " + data)
        temmRequest = datastore_pb2.Request(key=key, data=data, requestType=requestType)
        self.stub.put(temmRequest)
        # print("temReq = ", temReq)
        # return self.stub.put(temmRequest)
        return

    def get(self, key):
        print("*** Geting data from main database ***")
        print("Search key = " + key)
        return self.stub.get(datastore_pb2.GetRequest(key=key))


def run(host, port):
    '''
    Run the GRPC server
    '''
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    datastore_pb2_grpc.add_DatastoreServicer_to_server(MyDatastoreSlaveServicer(), server)
    server.add_insecure_port('%s:%d' % (host, port))
    server.start()

    try:
        while True:
            print("Server started at...%d" % port)
            client = MyDatastoreSlaveServicer()
            print("sssssssssssssss",client.slaveId, client.port)
            client.put("client.slaveId", "str(client.port)")
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    run('0.0.0.0', PORT)
