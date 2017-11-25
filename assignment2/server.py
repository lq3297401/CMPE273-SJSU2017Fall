'''
################################## server.py #############################
# Lab1 gRPC RocksDB Server
################################## server.py #############################
'''
import random
import time
import grpc
import datastore_pb2
import datastore_pb2_grpc
import uuid
import rocksdb

from concurrent import futures

_ONE_DAY_IN_SECONDS = 60 * 60 * 24

'''
Container
'''
put_tasks = []
delete_tasks = []
get_tasks = []

'''
Replicator decorator
'''

def my_replicator(some_function):
    def wrapper(*args, **kwargs):
        if args[1].requestInfo == 'put':
            print("------------ Inserting data to main server database -----------")
            for task in put_tasks:
                print("Inserting key = " + task.key + ", data = "+ task.data)
                yield task
            print("-----** Finish inserting **-----\n")
            put_tasks.clear()

        elif args[1].requestInfo == 'delete':
            print("------------ deleting data from main server database -----------")
            for task in delete_tasks:
                print("Deleting key = " + task.key + ", data = "+ task.data)
                yield task
            print("-----** Finish deleting **-----\n")
            delete_tasks.clear()

        elif args[1].requestInfo == 'get':
            print("------------ getting data from main server database -----------")
            for task in get_tasks:
                print("Getting data that key = " + task.key + ", data = "+ task.data)
                yield task
            print("-----** Finish getting **-----\n")
            get_tasks.clear()

        yield some_function(*args, **kwargs)
    return wrapper

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))

    def put(self, allRequests, context):
        for new_task in allRequests:
            self.db.put(new_task.key.encode(), new_task.data.encode())
            if new_task.data == self.db.get(new_task.key.encode()).decode():
                put_tasks.append(new_task)
            yield datastore_pb2.Response(key=new_task.key, data=new_task.data)

    def delete(self, allRequests, context):
        for new_task in allRequests:
            if self.db.get(new_task.key.encode()) == None:
                print("Didn't find the data which key = " + str(new_task.key.encode()))
            else:
                print("Deleting key = " + str(new_task.key.encode()) + ", value = ", self.db.get(new_task.key.encode()))
                self.db.delete(new_task.key.encode())
                # delete_tasks.append(new_task)
            yield datastore_pb2.Response(key=new_task.key, data=new_task.data)

    def get(self, allRequests, context):
        for new_task in allRequests:
            data=self.db.get(new_task.key.encode())
            if self.db.get(new_task.key.encode()) == None:
                print("Didn't find the data which key = " + str(new_task.key.encode()))
                # get_tasks.append(new_task)
            else:
                print("Searching key = " + str(new_task.key.encode()) + ", value = " + str(data))
            yield datastore_pb2.Response(key=new_task.key, data=data)

    @my_replicator
    def replicator(self, request, context):
        pass

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
