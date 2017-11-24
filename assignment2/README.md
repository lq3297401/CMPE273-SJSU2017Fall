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
  ```sh
    python server.py
  ```
  * 3. run slave server in the 2nd term:
  ```sh
    python serverSlave.py
  ```
  * 4. run client.py in the last term with following format for inserting data:\n
      I defined the host = 0.0.0.0, master server's port = 3000.\n
      Example: python client.py 0.0.0.0 3000 AAA aaa, so the key-value pair "AAA" "aaa" will be stored in server's database and also in the slave server's database.
  ```sh
    python client.py <host> <port> <key1> <value1>
  ```

  * 5. run client.py with following format for getting data:
    I defined the host = 0.0.0.0, master server's port = 3000, slave server's port = 6001\n
    Example: python client.py 0.0.0.0 3000 AAA, so the value pair of the key "AAA" "aaa" will be find.
  ```sh
    python serverSlave.py <host> <port> <key1>
  ```
