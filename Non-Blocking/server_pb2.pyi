from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Address(_message.Message):
    __slots__ = ["ip", "port"]
    IP_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    port: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[str] = ...) -> None: ...

class BackupDeleteRequest(_message.Message):
    __slots__ = ["timestamp", "uuid"]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    timestamp: str
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class BackupWriteRequest(_message.Message):
    __slots__ = ["content", "name", "timestamp", "uuid"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    content: str
    name: str
    timestamp: str
    uuid: str
    def __init__(self, name: _Optional[str] = ..., uuid: _Optional[str] = ..., content: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class DeleteAcknowledgement(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class DeleteRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class DeleteResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class ReadRequest(_message.Message):
    __slots__ = ["uuid"]
    UUID_FIELD_NUMBER: _ClassVar[int]
    uuid: str
    def __init__(self, uuid: _Optional[str] = ...) -> None: ...

class ReadResponse(_message.Message):
    __slots__ = ["content", "name", "status", "timestamp"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    content: str
    name: str
    status: str
    timestamp: str
    def __init__(self, status: _Optional[str] = ..., name: _Optional[str] = ..., content: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class Replica(_message.Message):
    __slots__ = ["address", "backup_replicas", "data_store", "directory", "name", "p_address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    BACKUP_REPLICAS_FIELD_NUMBER: _ClassVar[int]
    DATA_STORE_FIELD_NUMBER: _ClassVar[int]
    DIRECTORY_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    P_ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: Address
    backup_replicas: _containers.RepeatedCompositeFieldContainer[Address]
    data_store: _containers.RepeatedCompositeFieldContainer[data_object]
    directory: str
    name: str
    p_address: Address
    def __init__(self, name: _Optional[str] = ..., address: _Optional[_Union[Address, _Mapping]] = ..., p_address: _Optional[_Union[Address, _Mapping]] = ..., directory: _Optional[str] = ..., data_store: _Optional[_Iterable[_Union[data_object, _Mapping]]] = ..., backup_replicas: _Optional[_Iterable[_Union[Address, _Mapping]]] = ...) -> None: ...

class WriteAcknowledgement(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class WriteRequest(_message.Message):
    __slots__ = ["content", "name", "uuid"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    content: str
    name: str
    uuid: str
    def __init__(self, name: _Optional[str] = ..., content: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class WriteResponse(_message.Message):
    __slots__ = ["status", "timestamp", "uuid"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    status: str
    timestamp: str
    uuid: str
    def __init__(self, status: _Optional[str] = ..., timestamp: _Optional[str] = ..., uuid: _Optional[str] = ...) -> None: ...

class data_object(_message.Message):
    __slots__ = ["filename", "timestamp", "uuid"]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    UUID_FIELD_NUMBER: _ClassVar[int]
    filename: str
    timestamp: str
    uuid: str
    def __init__(self, uuid: _Optional[str] = ..., filename: _Optional[str] = ..., timestamp: _Optional[str] = ...) -> None: ...

class newReplicaRequest(_message.Message):
    __slots__ = ["address"]
    ADDRESS_FIELD_NUMBER: _ClassVar[int]
    address: Address
    def __init__(self, address: _Optional[_Union[Address, _Mapping]] = ...) -> None: ...

class newReplicaResponse(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...
