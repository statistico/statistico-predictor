# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: app/grpc/proto/team/team.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='app/grpc/proto/team/team.proto',
  package='team',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x61pp/grpc/proto/team/team.proto\x12\x04team\" \n\x04Team\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\tb\x06proto3')
)




_TEAM = _descriptor.Descriptor(
  name='Team',
  full_name='team.Team',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='team.Team.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='team.Team.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=40,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['Team'] = _TEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Team = _reflection.GeneratedProtocolMessageType('Team', (_message.Message,), dict(
  DESCRIPTOR = _TEAM,
  __module__ = 'app.grpc.proto.team.team_pb2'
  # @@protoc_insertion_point(class_scope:team.Team)
  ))
_sym_db.RegisterMessage(Team)


# @@protoc_insertion_point(module_scope)
