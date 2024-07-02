from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Blog(_message.Message):
    __slots__ = ("id", "title", "content", "created", "is_published", "user_id")
    ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    CREATED_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    title: str
    content: str
    created: _timestamp_pb2.Timestamp
    is_published: bool
    user_id: int
    def __init__(self, id: _Optional[int] = ..., title: _Optional[str] = ..., content: _Optional[str] = ..., created: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., is_published: bool = ..., user_id: _Optional[int] = ...) -> None: ...

class BlogRequest(_message.Message):
    __slots__ = ("id",)
    ID_FIELD_NUMBER: _ClassVar[int]
    id: int
    def __init__(self, id: _Optional[int] = ...) -> None: ...

class BlogListResponse(_message.Message):
    __slots__ = ("blogs",)
    BLOGS_FIELD_NUMBER: _ClassVar[int]
    blogs: _containers.RepeatedCompositeFieldContainer[Blog]
    def __init__(self, blogs: _Optional[_Iterable[_Union[Blog, _Mapping]]] = ...) -> None: ...

class BlogCreate(_message.Message):
    __slots__ = ("title", "content", "is_published", "user_id")
    TITLE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    IS_PUBLISHED_FIELD_NUMBER: _ClassVar[int]
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    title: str
    content: str
    is_published: bool
    user_id: int
    def __init__(self, title: _Optional[str] = ..., content: _Optional[str] = ..., is_published: bool = ..., user_id: _Optional[int] = ...) -> None: ...
