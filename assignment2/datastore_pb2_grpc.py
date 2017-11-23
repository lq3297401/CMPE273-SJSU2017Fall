# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import datastore_pb2 as datastore__pb2


class DatastoreStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.put = channel.unary_unary(
        '/Datastore/put',
        request_serializer=datastore__pb2.Request.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.get = channel.unary_unary(
        '/Datastore/get',
        request_serializer=datastore__pb2.GetRequest.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.sendInfo = channel.unary_unary(
        '/Datastore/sendInfo',
        request_serializer=datastore__pb2.SlaveRegisterRequest.SerializeToString,
        response_deserializer=datastore__pb2.SlaveRegisterResponse.FromString,
        )
    self.getInfo = channel.unary_unary(
        '/Datastore/getInfo',
        request_serializer=datastore__pb2.SlaveRegisterRequest.SerializeToString,
        response_deserializer=datastore__pb2.SlaveRegisterResponse.FromString,
        )


class DatastoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def sendInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def getInfo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatastoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'put': grpc.unary_unary_rpc_method_handler(
          servicer.put,
          request_deserializer=datastore__pb2.Request.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'get': grpc.unary_unary_rpc_method_handler(
          servicer.get,
          request_deserializer=datastore__pb2.GetRequest.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'sendInfo': grpc.unary_unary_rpc_method_handler(
          servicer.sendInfo,
          request_deserializer=datastore__pb2.SlaveRegisterRequest.FromString,
          response_serializer=datastore__pb2.SlaveRegisterResponse.SerializeToString,
      ),
      'getInfo': grpc.unary_unary_rpc_method_handler(
          servicer.getInfo,
          request_deserializer=datastore__pb2.SlaveRegisterRequest.FromString,
          response_serializer=datastore__pb2.SlaveRegisterResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Datastore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
