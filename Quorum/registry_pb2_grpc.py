# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import registry_pb2 as registry__pb2


class RegisterStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.registerServer = channel.unary_unary(
                '/Register/registerServer',
                request_serializer=registry__pb2.registerServerRequest.SerializeToString,
                response_deserializer=registry__pb2.registerServerResponse.FromString,
                )
        self.GetServerList = channel.unary_unary(
                '/Register/GetServerList',
                request_serializer=registry__pb2.ClientRequest.SerializeToString,
                response_deserializer=registry__pb2.ClientResponse.FromString,
                )


class RegisterServicer(object):
    """Missing associated documentation comment in .proto file."""

    def registerServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetServerList(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_RegisterServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'registerServer': grpc.unary_unary_rpc_method_handler(
                    servicer.registerServer,
                    request_deserializer=registry__pb2.registerServerRequest.FromString,
                    response_serializer=registry__pb2.registerServerResponse.SerializeToString,
            ),
            'GetServerList': grpc.unary_unary_rpc_method_handler(
                    servicer.GetServerList,
                    request_deserializer=registry__pb2.ClientRequest.FromString,
                    response_serializer=registry__pb2.ClientResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Register', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Register(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def registerServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Register/registerServer',
            registry__pb2.registerServerRequest.SerializeToString,
            registry__pb2.registerServerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetServerList(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Register/GetServerList',
            registry__pb2.ClientRequest.SerializeToString,
            registry__pb2.ClientResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
