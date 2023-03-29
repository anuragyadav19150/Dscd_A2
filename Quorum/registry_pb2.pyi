import server_pb2 as _server_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ClientRequest(_message.Message):
    __slots__ = ["client"]
    CLIENT_FIELD_NUMBER: _ClassVar[int]
    client: str
    def __init__(self, client: _Optional[str] = ...) -> None: ...

class ClientResponse(_message.Message):
    __slots__ = ["serverclient"]
    SERVERCLIENT_FIELD_NUMBER: _ClassVar[int]
    serverclient: _containers.RepeatedCompositeFieldContainer[_server_pb2.Server]
    def __init__(self, serverclient: _Optional[_Iterable[_Union[_server_pb2.Server, _Mapping]]] = ...) -> None: ...

class RegistryServer(_message.Message):
    __slots__ = ["N", "N_r", "N_w", "servers"]
    N: int
    N_FIELD_NUMBER: _ClassVar[int]
    N_R_FIELD_NUMBER: _ClassVar[int]
    N_W_FIELD_NUMBER: _ClassVar[int]
    N_r: int
    N_w: int
    SERVERS_FIELD_NUMBER: _ClassVar[int]
    servers: _containers.RepeatedCompositeFieldContainer[_server_pb2.Server]
    def __init__(self, servers: _Optional[_Iterable[_Union[_server_pb2.Server, _Mapping]]] = ..., N_r: _Optional[int] = ..., N_w: _Optional[int] = ..., N: _Optional[int] = ...) -> None: ...

class registerServerRequest(_message.Message):
    __slots__ = ["server"]
    SERVER_FIELD_NUMBER: _ClassVar[int]
    server: _server_pb2.Server
    def __init__(self, server: _Optional[_Union[_server_pb2.Server, _Mapping]] = ...) -> None: ...

class registerServerResponse(_message.Message):
    __slots__ = ["response"]
    RESPONSE_FIELD_NUMBER: _ClassVar[int]
    response: str
    def __init__(self, response: _Optional[str] = ...) -> None: ...
