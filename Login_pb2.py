# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Login.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Login.proto',
  package='',
  serialized_pb=_b('\n\x0bLogin.proto\"R\n\x08\x43\x32SLogin\x12\x0f\n\x07\x61\x63\x63ount\x18\x01 \x01(\t\x12\x12\n\nconnectKey\x18\x02 \x01(\t\x12\x0e\n\x06platId\x18\x03 \x01(\x05\x12\x11\n\tplatToken\x18\x04 \x01(\t\"P\n\x08S2CLogin\x12\x0e\n\x06result\x18\x01 \x01(\x05\x12\x10\n\x08playerId\x18\x02 \x01(\x03\x12\x0c\n\x04name\x18\x03 \x01(\t\x12\x14\n\x0creconnectKey\x18\x04 \x01(\tB7\n\'com.janlr.ag.cellwar.common.fixed.protoB\nLoginProtoH\x03')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_C2SLOGIN = _descriptor.Descriptor(
  name='C2SLogin',
  full_name='C2SLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='account', full_name='C2SLogin.account', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='connectKey', full_name='C2SLogin.connectKey', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platId', full_name='C2SLogin.platId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='platToken', full_name='C2SLogin.platToken', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=15,
  serialized_end=97,
)


_S2CLOGIN = _descriptor.Descriptor(
  name='S2CLogin',
  full_name='S2CLogin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='result', full_name='S2CLogin.result', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='playerId', full_name='S2CLogin.playerId', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='S2CLogin.name', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reconnectKey', full_name='S2CLogin.reconnectKey', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=99,
  serialized_end=179,
)

DESCRIPTOR.message_types_by_name['C2SLogin'] = _C2SLOGIN
DESCRIPTOR.message_types_by_name['S2CLogin'] = _S2CLOGIN

C2SLogin = _reflection.GeneratedProtocolMessageType('C2SLogin', (_message.Message,), dict(
  DESCRIPTOR = _C2SLOGIN,
  __module__ = 'Login_pb2'
  # @@protoc_insertion_point(class_scope:C2SLogin)
  ))
_sym_db.RegisterMessage(C2SLogin)

S2CLogin = _reflection.GeneratedProtocolMessageType('S2CLogin', (_message.Message,), dict(
  DESCRIPTOR = _S2CLOGIN,
  __module__ = 'Login_pb2'
  # @@protoc_insertion_point(class_scope:S2CLogin)
  ))
_sym_db.RegisterMessage(S2CLogin)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\'com.janlr.ag.cellwar.common.fixed.protoB\nLoginProtoH\003'))
# @@protoc_insertion_point(module_scope)
