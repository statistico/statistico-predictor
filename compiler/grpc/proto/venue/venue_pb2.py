# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/venue/venue.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/venue/venue.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n%compiler/grpc/proto/venue/venue.proto\x12\x05proto\x1a\x1egoogle/protobuf/wrappers.proto\"\\\n\x05Venue\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValueb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_VENUE = _descriptor.Descriptor(
  name='Venue',
  full_name='proto.Venue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.Venue.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Venue.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=80,
  serialized_end=172,
)

_VENUE.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_VENUE.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Venue'] = _VENUE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Venue = _reflection.GeneratedProtocolMessageType('Venue', (_message.Message,), dict(
  DESCRIPTOR = _VENUE,
  __module__ = 'compiler.grpc.proto.venue.venue_pb2'
  # @@protoc_insertion_point(class_scope:proto.Venue)
  ))
_sym_db.RegisterMessage(Venue)


# @@protoc_insertion_point(module_scope)
