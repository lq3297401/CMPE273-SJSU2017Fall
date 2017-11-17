# This folder is for SJSU CMPE273 2017 Fall Course
Assignment for SJSU CMPE 273

* **Lab1** is to Implement a **key-value** store gRPC service using RocksDB
  * RocksDB native - https://github.com/facebook/rocksdb/blob/master/INSTALL.md
  * gRPC Docker - https://github.com/grpc/grpc-docker-library/tree/master/1.4/python

* **Assignment1** is to implement a dynamic Python invoker REST service.
The service will have the following features:
  * Python Script Uploader
POST http://localhost:8000/api/v1/scripts
  * Python Script Invoker
GET http://localhost:8000/api/v1/scripts/{script-id}
