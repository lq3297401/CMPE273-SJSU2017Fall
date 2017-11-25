# Assignment 2 for SJSU CMPE 273

* **Assignment2** is to implement a RocksDB replication in Python using the design from
[Rocksplicator](https://medium.com/@Pinterest_Engineering/open-sourcing-rocksplicator-a-real-time-rocksdb-data-replicator-558cd3847a9d). You can use Lab 1 as a based line. Differences form the replicator are:
  * You will be using GRPC Python server instead of Thrift server.
  * You will be exploring more into GRPC sync, async, and streaming.
  * You can ignore all cluster management features from the replicator.

  * 1. Go to the file folder and build docker file:
  ```sh
    docker build -t 273web:1.0 .
  ```
  * 2. Go to the file folder and build docker bridge:
  ```sh
    docker network create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1 dockernet
  ```
  * 3. Go to the file folder and build .proto:
  ```sh
    docker run -it --rm --name grpc-tools -v "$PWD":/usr/src/myapp -w /usr/src/myapp 273web:1.0 python3.6 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto
  ```
  * 4. run server.py in the 1st term:
  ```sh
    docker run -p 3000:3000 -it --rm --name lab1-server -v "$PWD":/usr/src/myapp -w /usr/src/myapp 273web:1.0 python3.6 server.py
  ```
  * 5. run client.py in the 2nd term:
  ```sh
    docker run -it --rm --name lab1-client -v "$PWD":/usr/src/myapp -w /usr/src/myapp 273web:1.0 python3.6 client.py 192.168.0.1
  ```
  I write the slaveServer inside the client.py as the design that professor suggested. When run the client.py, the system will generate random number and string as the key-value pair to test put, get and delete function, also I defined 2 pair of fixed key-value pair: ("testKey1", "testValue1"), ("testKey2", "testValue2") for get and delete testing.
