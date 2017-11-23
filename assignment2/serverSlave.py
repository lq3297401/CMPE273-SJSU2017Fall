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

PORT = 3000
# class MyDatastoreSlaveServicer():
class MyDatastoreSlaveServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.channel = grpc.insecure_channel('%s:%d' % ('0.0.0.0', PORT))
        self.stub = datastore_pb2_grpc.DatastoreStub(self.channel)

        # os.system('rm serverSlave.db/LOCK')
        # self.db = rocksdb.DB("serverSlave.db", rocksdb.Options(create_if_missing=True))
        self.slaveId="1"
        self.port=str(PORT)


        print("-------- Slave server start --------")


    def sendInfo(self, slaveId, port):
        print("*** Sending slaveServer slaveId and port to main server ***")
        # temmRequest = datastore_pb2.SlaveRegisterRequest(slaveId=slaveId, port=port)
        temmRequest = datastore_pb2.SlaveRegisterRequest(slaveId=slaveId, port=port)
        print("SlaveServer infor sending", temmRequest)
        # rpc sendInfo(SlaveRegisterRequest) returns (SlaveRegisterResponse) {}
        return datastore_pb2.SlaveRegisterResponse(slaveId=slaveId, port=port)

    def getInfo(self, request, context):
        '''
        get slave register information
        '''
        print("-------- Slave server information --------")
        print(request)
        print("slaveId = " + request.slaveId, "port = " + request.port)
        return datastore_pb2.SlaveRegisterResponse(slaveId=request.slaveId, port=request.port)
        # print("-------- Slave server information --------")
        # print(request)
        # print("slaveId = " + request.slaveId, "port = " + request.port)
        # registerInfo[request.slaveId] = request.port
        # temmRequest = datastore_pb2.Request(slaveId=request.slaveId, port=request.port)
        # # print("temReq = ", temReq)
        # return self.stub.getInfo(temmRequest)
        # dict = {'SlaveServer slaveId': request.slaveId, 'SlaveServer port': request.port}
        # print "SlaveServer slaveId: ", dict['SlaveServer slaveId'], "SlaveServer port: ", dict[request.port]




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
            client.sendInfo(client.slaveId, client.port)
            client.put(client.slaveId, client.port)
            # response = client.get(searchKey)
            # print(response)
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == '__main__':
    # client = MyDatastoreSlaveServicer()
    # client.sendInfo(client.slaveId, client.port)
    run('0.0.0.0', PORT)

    # print( ", client.slaveId", client.slaveId, ", client.port", client.port)

    # client.run(localhost,PORT)
