import server_pb2 as _server_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class ClientResponse(_message.Message):
    __slots__ = ["addresses", "status"]
    ADDRESSES_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    addresses: _containers.RepeatedCompositeFieldContainer[_server_pb2.Address]
    status: str
    def __init__(self, status: _Optional[str] = ..., addresses: _Optional[_Iterable[_Union[_server_pb2.Address, _Mapping]]] = ...) -> None: ...

class RegistryServer(_message.Message):
    __slots__ = ["p_address", "replicas"]
    P_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    REPLICAS_FIELD_NUMBER: _ClassVar[int]
    p_address: _server_pb2.Address
    replicas: _containers.RepeatedCompositeFieldContainer[_server_pb2.Address]
    def __init__(self, replicas: _Optional[_Iterable[_Union[_server_pb2.Address, _Mapping]]] = ..., p_address: _Optional[_Union[_server_pb2.Address, _Mapping]] = ...) -> None: ...

class registerReplicaRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: _server_pb2.Address
    def __init__(self, address: _Optional[_Union[_server_pb2.Address, _Mapping]] = ...) -> None: ...

class registerReplicaResponse(_message.Message):
    __slots__ = ["paddress", "status"]
    PADDRESS_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    paddress: _server_pb2.Address
    status: str
    def __init__(self, status: _Optional[str] = ..., paddress: _Optional[_Union[_server_pb2.Address, _Mapping]] = ...) -> None: ...
