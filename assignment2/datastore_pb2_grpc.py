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
    self.sync = channel.unary_unary(
        '/Datastore/sync',
        request_serializer=datastore__pb2.SyncRequest.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
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
    self.delete = channel.unary_unary(
        '/Datastore/delete',
        request_serializer=datastore__pb2.DeleteRequest.SerializeToString,
        response_deserializer=datastore__pb2.DeleteMsg.FromString,
        )


class DatastoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def sync(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

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

  def delete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatastoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'sync': grpc.unary_unary_rpc_method_handler(
          servicer.sync,
          request_deserializer=datastore__pb2.SyncRequest.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
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
      'delete': grpc.unary_unary_rpc_method_handler(
          servicer.delete,
          request_deserializer=datastore__pb2.DeleteRequest.FromString,
          response_serializer=datastore__pb2.DeleteMsg.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Datastore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
