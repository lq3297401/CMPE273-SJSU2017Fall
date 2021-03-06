### This is Lab1 for SJSU CMPE 273 - 2017 Fall course of Professor Si Thu Aung

### My Output on Client

![Lab1_ClientOutput_Qi](https://github.com/lq3297401/CMPE273-SJSU2017Fall/blob/master/Lab1/Lab1_ClientOutput_Qi%20Liu.jpg?raw=true)

```sh
Client is connecting to Server at 192.168.0.1:3000...
## PUT Request: value = foo
## PUT Response: key = 94ccdd436c9b467baf6799fb6fbcf275
## GET Request: key = 94ccdd436c9b467baf6799fb6fbcf275
## GET Response: value = foo
```

```sh
Client is connecting to Server at 192.168.0.1:3000...
## PUT Request: value = foo
## PUT Response: key = 7e01736938644ce88f7ea460e57f04b5
## GET Request: key = 7e01736938644ce88f7ea460e57f04b5
## GET Response: value = foo
```

### Processes:

* Create a Docker image from Dockerfile from Professor Si Thu Aung's example: [Build a Docker Image with RocksDB and gRPC](https://github.com/sithu/cmpe273-fall17/tree/master/docker).

* Create a Docker network so that each container can connect to the host under the fixed IP 192.168.0.1.

```sh
docker network create -d bridge --subnet 192.168.0.0/24 --gateway 192.168.0.1 dockernet
```

* Run the server and client containers.

```sh
# Generate Stub for client and server
docker run -it --rm --name grpc-tools -v $(pwd):/usr/src/myapp -w /usr/src/myapp qi_273_lab1:latest python3.6 -m grpc.tools.protoc -I. --python_out=. --grpc_python_out=. datastore.proto


# Server
docker run -p 3000:3000 -it --rm --name lab1-server -v $(pwd):/usr/src/myapp -w /usr/src/myapp qi_273_lab1:latest python3.6 server.py


# Client
docker run -it --rm --name lab1-client -v $(pwd):/usr/src/myapp -w /usr/src/myapp qi_273_lab1:latest python3.6 client.py 192.168.0.1
```
