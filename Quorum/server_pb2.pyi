from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Server(_message.Message):
    __slots__ = ["ip", "name", "port"]
    IP_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    PORT_FIELD_NUMBER: _ClassVar[int]
    ip: str
    name: str
    port: str
    def __init__(self, ip: _Optional[str] = ..., port: _Optional[str] = ..., name: _Optional[str] = ...) -> None: ...

class clientResponse(_message.Message):
    __slots__ = ["content", "filename", "uid"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FILENAME_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    content: str
    filename: str
    uid: str
    def __init__(self, uid: _Optional[str] = ..., filename: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class clientResponseDelete(_message.Message):
    __slots__ = ["uid", "work"]
    UID_FIELD_NUMBER: _ClassVar[int]
    WORK_FIELD_NUMBER: _ClassVar[int]
    uid: str
    work: str
    def __init__(self, uid: _Optional[str] = ..., work: _Optional[str] = ...) -> None: ...

class clientResponseRead(_message.Message):
    __slots__ = ["uid"]
    UID_FIELD_NUMBER: _ClassVar[int]
    uid: str
    def __init__(self, uid: _Optional[str] = ...) -> None: ...

class serverResponse(_message.Message):
    __slots__ = ["status", "uid", "version"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    status: str
    uid: str
    version: str
    def __init__(self, uid: _Optional[str] = ..., status: _Optional[str] = ..., version: _Optional[str] = ...) -> None: ...

class serverResponseDelete(_message.Message):
    __slots__ = ["status"]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    status: str
    def __init__(self, status: _Optional[str] = ...) -> None: ...

class serverResponseRead(_message.Message):
    __slots__ = ["content", "status", "uid", "version"]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    UID_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    content: str
    status: str
    uid: str
    version: str
    def __init__(self, uid: _Optional[str] = ..., status: _Optional[str] = ..., version: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...
