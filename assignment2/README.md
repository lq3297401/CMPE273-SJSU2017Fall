# Assignment 2 for SJSU CMPE 273

* **Assignment2** is to implement a RocksDB replication in Python using the design from
[Rocksplicator](https://medium.com/@Pinterest_Engineering/open-sourcing-rocksplicator-a-real-time-rocksdb-data-replicator-558cd3847a9d). You can use Lab 1 as a based line. Differences form the replicator are:
  * You will be using GRPC Python server instead of Thrift server.
  * You will be exploring more into GRPC sync, async, and streaming.
  * You can ignore all cluster management features from the replicator.

  * 1. Go to the file folder and build .proto:
```sh
  python -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto
```
  * 2. run server.py in the 1st term:
  python server.py

  * 3. run slave server in the 2nd term:
  python serverSlave.py"

  * 4. run client.py in the last term with following format for inserting data:
  python client.py <key> <value>
  Example: python client.py AAA aaa \n
  So the key-value pair "AAA" "aaa" will be stored in server's database // also in the slave server's database.

  * 5. run client.py in the last term with following format for inserting data:
  python client.py <key>
  Example: python client.py AAA \n
  So the value pair of the key "AAA" "aaa" will be find and show on both client and server
