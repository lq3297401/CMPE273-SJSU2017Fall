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
get_tasks = []
delete_tasks = []

'''
Replicator decorator
'''

def replicator(a_function_to_decorate):
    def the_wrapper_around_the_original_function(*args, **kwargs):
        if args[1].requestInfo == 'put':
            print("---- Sending put request to slave server ----")
            for task in put_tasks:
                print("Inserting key = " + task.key + ", data = "+ task.data)
                yield task
            print("---- Finish sending put request ----\n")
            put_tasks.clear()

        elif args[1].requestInfo == 'get':
            print("---- Sending get request to slave server -----------")
            for task in get_tasks:
                print("Getting data that key = " + task.key)
                yield task
            print("---- Finish sending get request ----\n")
            get_tasks.clear()

        elif args[1].requestInfo == 'delete':
            print("---- Sending deleting request to slave server ----")
            for task in delete_tasks:
                print("Deleting key = " + task.key)
                yield task
            print("---- Finish sending delete request ----\n")
            delete_tasks.clear()

        yield a_function_to_decorate(*args, **kwargs)
    return the_wrapper_around_the_original_function

class MyDatastoreServicer(datastore_pb2.DatastoreServicer):
    def __init__(self):
        self.db = rocksdb.DB("server.db", rocksdb.Options(create_if_missing=True))

    def put(self, allRequests, context):
        print("------------ Inserting data to main server database -----------")
        for new_task in allRequests:
            print("Inserting key = " + str(new_task.key.encode()) + ", data = " + str(new_task.data.encode()))
            self.db.put(new_task.key.encode(), new_task.data.encode())
            if new_task.data == self.db.get(new_task.key.encode()).decode():
                put_tasks.append(new_task)
            yield datastore_pb2.Response(key=new_task.key, data=new_task.data)
        print("-----** Finish inserting **-----\n")

    def get(self, allRequests, context):
        print("------------ getting data from main server database -----------")
        for new_task in allRequests:
            data=self.db.get(new_task.key.encode())
            if self.db.get(new_task.key.encode()) == None:
                print("Didn't find the data which key = " + str(new_task.key.encode()))
            else:
                print("Searching key = " + str(new_task.key.encode()) + ", value = " + str(data))
                get_tasks.append(new_task)
            yield datastore_pb2.Response(key=new_task.key, data=data)
        print("-----** Finish getting **-----\n")

    def delete(self, allRequests, context):
        print("------------ deleting data from main server database -----------")
        for new_task in allRequests:
            if self.db.get(new_task.key.encode()) == None:
                print("Didn't find the data which key = " + str(new_task.key.encode()))
            else:
                print("Deleting key = " + str(new_task.key.encode()) + ", value = ", self.db.get(new_task.key.encode()))
                self.db.delete(new_task.key.encode())
                delete_tasks.append(new_task)
            yield datastore_pb2.Response(key=new_task.key, data=new_task.data)
        print("-----** Finish deleting **-----\n")

    @replicator
    def replicator(self, request, context):
        print("** Here the replicator starts **")
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
