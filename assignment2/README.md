# Assignment 2 for SJSU CMPE 273

* **Assignment2** is to implement a RocksDB replication in Python using the design from
[Rocksplicator](https://medium.com/@Pinterest_Engineering/open-sourcing-rocksplicator-a-real-time-rocksdb-data-replicator-558cd3847a9d). You can use Lab 1 as a based line. Differences form the replicator are:
  * You will be using GRPC Python server instead of Thrift server.
  * You will be exploring more into GRPC sync, async, and streaming.
  * You can ignore all cluster management features from the replicator.
