# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class Server_serviceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.WriteServer = channel.unary_unary(
                '/Server_service/WriteServer',
                request_serializer=server__pb2.clientResponse.SerializeToString,
                response_deserializer=server__pb2.serverResponse.FromString,
                )
        self.ReadServer = channel.unary_unary(
                '/Server_service/ReadServer',
                request_serializer=server__pb2.clientResponseRead.SerializeToString,
                response_deserializer=server__pb2.serverResponseRead.FromString,
                )
        self.DeleteServer = channel.unary_unary(
                '/Server_service/DeleteServer',
                request_serializer=server__pb2.clientResponseDelete.SerializeToString,
                response_deserializer=server__pb2.serverResponseDelete.FromString,
                )


class Server_serviceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def WriteServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ReadServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteServer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Server_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'WriteServer': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteServer,
                    request_deserializer=server__pb2.clientResponse.FromString,
                    response_serializer=server__pb2.serverResponse.SerializeToString,
            ),
            'ReadServer': grpc.unary_unary_rpc_method_handler(
                    servicer.ReadServer,
                    request_deserializer=server__pb2.clientResponseRead.FromString,
                    response_serializer=server__pb2.serverResponseRead.SerializeToString,
            ),
            'DeleteServer': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteServer,
                    request_deserializer=server__pb2.clientResponseDelete.FromString,
                    response_serializer=server__pb2.serverResponseDelete.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Server_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server_service(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def WriteServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/WriteServer',
            server__pb2.clientResponse.SerializeToString,
            server__pb2.serverResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ReadServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/ReadServer',
            server__pb2.clientResponseRead.SerializeToString,
            server__pb2.serverResponseRead.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteServer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/DeleteServer',
            server__pb2.clientResponseDelete.SerializeToString,
            server__pb2.serverResponseDelete.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
