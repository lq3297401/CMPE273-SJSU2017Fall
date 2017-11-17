# This folder is for SJSU CMPE273 2017 Fall Course
Labs/Assignment for SJSU CMPE 273 2017 fall

* **Lab1** is to Implement a **key-value** store gRPC service using RocksDB
  * RocksDB native - https://github.com/facebook/rocksdb/blob/master/INSTALL.md
  * gRPC Docker - https://github.com/grpc/grpc-docker-library/tree/master/1.4/python

* **Assignment1** is to implement a dynamic Python invoker REST service.<br />
The service will have the following features:
  * Python Script Uploader <br />
POST http://localhost:8000/api/v1/scripts
  * Python Script Invoker <br />
GET http://localhost:8000/api/v1/scripts/{script-id}

* **Assignment2** is to implement a RocksDB replication in Python using the design from
[Rocksplicator](https://medium.com/@Pinterest_Engineering/open-sourcing-rocksplicator-a-real-time-rocksdb-data-replicator-558cd3847a9d). You can use Lab 1 as a based line. Differences form the replicator are:
  * You will be using GRPC Python server instead of Thrift server.
  * You will be exploring more into GRPC sync, async, and streaming.
  * You can ignore all cluster management features from the replicator.
