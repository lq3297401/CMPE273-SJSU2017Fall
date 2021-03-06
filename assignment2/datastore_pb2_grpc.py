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
    self.put = channel.stream_stream(
        '/Datastore/put',
        request_serializer=datastore__pb2.Request.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.delete = channel.stream_stream(
        '/Datastore/delete',
        request_serializer=datastore__pb2.Request.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.get = channel.stream_stream(
        '/Datastore/get',
        request_serializer=datastore__pb2.Request.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )
    self.replicator = channel.unary_stream(
        '/Datastore/replicator',
        request_serializer=datastore__pb2.PullRequest.SerializeToString,
        response_deserializer=datastore__pb2.Response.FromString,
        )


class DatastoreServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def put(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def delete(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def get(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def replicator(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_DatastoreServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'put': grpc.stream_stream_rpc_method_handler(
          servicer.put,
          request_deserializer=datastore__pb2.Request.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'delete': grpc.stream_stream_rpc_method_handler(
          servicer.delete,
          request_deserializer=datastore__pb2.Request.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'get': grpc.stream_stream_rpc_method_handler(
          servicer.get,
          request_deserializer=datastore__pb2.Request.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
      'replicator': grpc.unary_stream_rpc_method_handler(
          servicer.replicator,
          request_deserializer=datastore__pb2.PullRequest.FromString,
          response_serializer=datastore__pb2.Response.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Datastore', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
