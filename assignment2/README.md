# Assignment 2 for SJSU CMPE 273

* **Assignment2** is to implement a RocksDB replication in Python using the design from
[Rocksplicator](https://medium.com/@Pinterest_Engineering/open-sourcing-rocksplicator-a-real-time-rocksdb-data-replicator-558cd3847a9d). You can use Lab 1 as a based line. Differences form the replicator are:
  * You will be using GRPC Python server instead of Thrift server.
  * You will be exploring more into GRPC sync, async, and streaming.
  * You can ignore all cluster management features from the replicator.



  1. Go to the file folder and build .proto:
```sh
  python -m grpc.tools.protoc -I. --python_out=. -rpc_python_out=. datastore.proto
```
  2. run server.py in the 1st term
  python server.py

  3. run follower server in the 2nd term


  4. run client.py in the last term with following format:

  Example for inserting key-value data: python client.py key1 value1 \n
  Example for getting data from database by key1: python client.py key1
