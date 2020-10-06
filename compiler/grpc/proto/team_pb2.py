# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/team.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from compiler.grpc.proto import requests_pb2 as compiler_dot_grpc_dot_proto_dot_requests__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/team.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x1e\x63ompiler/grpc/proto/team.proto\x12\x05proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\"compiler/grpc/proto/requests.proto\"\x89\x02\n\x04Team\x12\n\n\x02id\x18\x01 \x01(\x04\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x30\n\nshort_code\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x12\n\ncountry_id\x18\x04 \x01(\x04\x12\x10\n\x08venue_id\x18\x05 \x01(\x04\x12\x34\n\x10is_national_team\x18\x06 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12-\n\x07\x66ounded\x18\x07 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12*\n\x04logo\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue2\x81\x01\n\x0bTeamService\x12\x30\n\x0bGetTeamByID\x12\x12.proto.TeamRequest\x1a\x0b.proto.Team\"\x00\x12@\n\x12GetTeamsBySeasonId\x12\x19.proto.SeasonTeamsRequest\x1a\x0b.proto.Team\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_requests__pb2.DESCRIPTOR,])




_TEAM = _descriptor.Descriptor(
  name='Team',
  full_name='proto.Team',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='proto.Team.id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='proto.Team.name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='short_code', full_name='proto.Team.short_code', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='country_id', full_name='proto.Team.country_id', index=3,
      number=4, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='venue_id', full_name='proto.Team.venue_id', index=4,
      number=5, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_national_team', full_name='proto.Team.is_national_team', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='founded', full_name='proto.Team.founded', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='logo', full_name='proto.Team.logo', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=110,
  serialized_end=375,
)

_TEAM.fields_by_name['short_code'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_TEAM.fields_by_name['is_national_team'].message_type = google_dot_protobuf_dot_wrappers__pb2._BOOLVALUE
_TEAM.fields_by_name['founded'].message_type = google_dot_protobuf_dot_wrappers__pb2._UINT64VALUE
_TEAM.fields_by_name['logo'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
DESCRIPTOR.message_types_by_name['Team'] = _TEAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Team = _reflection.GeneratedProtocolMessageType('Team', (_message.Message,), dict(
  DESCRIPTOR = _TEAM,
  __module__ = 'compiler.grpc.proto.team_pb2'
  # @@protoc_insertion_point(class_scope:proto.Team)
  ))
_sym_db.RegisterMessage(Team)



_TEAMSERVICE = _descriptor.ServiceDescriptor(
  name='TeamService',
  full_name='proto.TeamService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=378,
  serialized_end=507,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetTeamByID',
    full_name='proto.TeamService.GetTeamByID',
    index=0,
    containing_service=None,
    input_type=compiler_dot_grpc_dot_proto_dot_requests__pb2._TEAMREQUEST,
    output_type=_TEAM,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetTeamsBySeasonId',
    full_name='proto.TeamService.GetTeamsBySeasonId',
    index=1,
    containing_service=None,
    input_type=compiler_dot_grpc_dot_proto_dot_requests__pb2._SEASONTEAMSREQUEST,
    output_type=_TEAM,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TEAMSERVICE)

DESCRIPTOR.services_by_name['TeamService'] = _TEAMSERVICE

# @@protoc_insertion_point(module_scope)
