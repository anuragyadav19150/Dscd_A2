# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import server_pb2 as server__pb2


class Server_serviceStub(object):
    """service Client_service{
    rpc Write (WriteRequest) returns (WriteResponse) {}

    rpc Read (ReadRequest) returns (ReadResponse) {}

    rpc Delete (DeleteRequest) returns (DeleteResponse) {}

    }

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.newReplica = channel.unary_unary(
                '/Server_service/newReplica',
                request_serializer=server__pb2.newReplicaRequest.SerializeToString,
                response_deserializer=server__pb2.newReplicaResponse.FromString,
                )
        self.WriteRequestToPrimary = channel.unary_unary(
                '/Server_service/WriteRequestToPrimary',
                request_serializer=server__pb2.WriteRequest.SerializeToString,
                response_deserializer=server__pb2.WriteResponse.FromString,
                )
        self.DeleteRequestToPrimary = channel.unary_unary(
                '/Server_service/DeleteRequestToPrimary',
                request_serializer=server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=server__pb2.DeleteResponse.FromString,
                )
        self.WriteRequestToBackup = channel.unary_unary(
                '/Server_service/WriteRequestToBackup',
                request_serializer=server__pb2.BackupWriteRequest.SerializeToString,
                response_deserializer=server__pb2.WriteAcknowledgement.FromString,
                )
        self.DeleteRequestToBackup = channel.unary_unary(
                '/Server_service/DeleteRequestToBackup',
                request_serializer=server__pb2.BackupDeleteRequest.SerializeToString,
                response_deserializer=server__pb2.DeleteAcknowledgement.FromString,
                )
        self.Write = channel.unary_unary(
                '/Server_service/Write',
                request_serializer=server__pb2.WriteRequest.SerializeToString,
                response_deserializer=server__pb2.WriteResponse.FromString,
                )
        self.Read = channel.unary_unary(
                '/Server_service/Read',
                request_serializer=server__pb2.ReadRequest.SerializeToString,
                response_deserializer=server__pb2.ReadResponse.FromString,
                )
        self.Delete = channel.unary_unary(
                '/Server_service/Delete',
                request_serializer=server__pb2.DeleteRequest.SerializeToString,
                response_deserializer=server__pb2.DeleteResponse.FromString,
                )


class Server_serviceServicer(object):
    """service Client_service{
    rpc Write (WriteRequest) returns (WriteResponse) {}

    rpc Read (ReadRequest) returns (ReadResponse) {}

    rpc Delete (DeleteRequest) returns (DeleteResponse) {}

    }

    """

    def newReplica(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteRequestToPrimary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRequestToPrimary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WriteRequestToBackup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteRequestToBackup(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Write(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Read(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Delete(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_Server_serviceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'newReplica': grpc.unary_unary_rpc_method_handler(
                    servicer.newReplica,
                    request_deserializer=server__pb2.newReplicaRequest.FromString,
                    response_serializer=server__pb2.newReplicaResponse.SerializeToString,
            ),
            'WriteRequestToPrimary': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteRequestToPrimary,
                    request_deserializer=server__pb2.WriteRequest.FromString,
                    response_serializer=server__pb2.WriteResponse.SerializeToString,
            ),
            'DeleteRequestToPrimary': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRequestToPrimary,
                    request_deserializer=server__pb2.DeleteRequest.FromString,
                    response_serializer=server__pb2.DeleteResponse.SerializeToString,
            ),
            'WriteRequestToBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.WriteRequestToBackup,
                    request_deserializer=server__pb2.BackupWriteRequest.FromString,
                    response_serializer=server__pb2.WriteAcknowledgement.SerializeToString,
            ),
            'DeleteRequestToBackup': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteRequestToBackup,
                    request_deserializer=server__pb2.BackupDeleteRequest.FromString,
                    response_serializer=server__pb2.DeleteAcknowledgement.SerializeToString,
            ),
            'Write': grpc.unary_unary_rpc_method_handler(
                    servicer.Write,
                    request_deserializer=server__pb2.WriteRequest.FromString,
                    response_serializer=server__pb2.WriteResponse.SerializeToString,
            ),
            'Read': grpc.unary_unary_rpc_method_handler(
                    servicer.Read,
                    request_deserializer=server__pb2.ReadRequest.FromString,
                    response_serializer=server__pb2.ReadResponse.SerializeToString,
            ),
            'Delete': grpc.unary_unary_rpc_method_handler(
                    servicer.Delete,
                    request_deserializer=server__pb2.DeleteRequest.FromString,
                    response_serializer=server__pb2.DeleteResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Server_service', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Server_service(object):
    """service Client_service{
    rpc Write (WriteRequest) returns (WriteResponse) {}

    rpc Read (ReadRequest) returns (ReadResponse) {}

    rpc Delete (DeleteRequest) returns (DeleteResponse) {}

    }

    """

    @staticmethod
    def newReplica(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/newReplica',
            server__pb2.newReplicaRequest.SerializeToString,
            server__pb2.newReplicaResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteRequestToPrimary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/WriteRequestToPrimary',
            server__pb2.WriteRequest.SerializeToString,
            server__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRequestToPrimary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/DeleteRequestToPrimary',
            server__pb2.DeleteRequest.SerializeToString,
            server__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def WriteRequestToBackup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/WriteRequestToBackup',
            server__pb2.BackupWriteRequest.SerializeToString,
            server__pb2.WriteAcknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteRequestToBackup(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/DeleteRequestToBackup',
            server__pb2.BackupDeleteRequest.SerializeToString,
            server__pb2.DeleteAcknowledgement.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Write(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/Write',
            server__pb2.WriteRequest.SerializeToString,
            server__pb2.WriteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Read(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/Read',
            server__pb2.ReadRequest.SerializeToString,
            server__pb2.ReadResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Delete(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Server_service/Delete',
            server__pb2.DeleteRequest.SerializeToString,
            server__pb2.DeleteResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
