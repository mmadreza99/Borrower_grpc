# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/borrwor.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/borrwor.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x13proto/borrwor.proto\"0\n\x0f\x42orrowerRequest\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x11\n\tn_account\x18\x02 \x01(\x05\"#\n\x10\x42orrowerResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2<\n\x06\x42orrow\x12\x32\n\x0bRequestLoan\x12\x10.BorrowerRequest\x1a\x11.BorrowerResponseb\x06proto3'
)

_BORROWERREQUEST = _descriptor.Descriptor(
  name='BorrowerRequest',
  full_name='BorrowerRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='Id', full_name='BorrowerRequest.Id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='n_account', full_name='BorrowerRequest.n_account', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=23,
  serialized_end=71,
)

_BORROWERRESPONSE = _descriptor.Descriptor(
  name='BorrowerResponse',
  full_name='BorrowerResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='BorrowerResponse.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=73,
  serialized_end=108,
)

DESCRIPTOR.message_types_by_name['BorrowerRequest'] = _BORROWERREQUEST
DESCRIPTOR.message_types_by_name['BorrowerResponse'] = _BORROWERRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BorrowerRequest = _reflection.GeneratedProtocolMessageType('BorrowerRequest', (_message.Message,), {
  'DESCRIPTOR' : _BORROWERREQUEST,
  '__module__' : 'proto.borrwor_pb2'
  # @@protoc_insertion_point(class_scope:BorrowerRequest)
  })
_sym_db.RegisterMessage(BorrowerRequest)

BorrowerResponse = _reflection.GeneratedProtocolMessageType('BorrowerResponse', (_message.Message,), {
  'DESCRIPTOR' : _BORROWERRESPONSE,
  '__module__' : 'proto.borrwor_pb2'
  # @@protoc_insertion_point(class_scope:BorrowerResponse)
  })
_sym_db.RegisterMessage(BorrowerResponse)

_BORROW = _descriptor.ServiceDescriptor(
  name='Borrow',
  full_name='Borrow',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=110,
  serialized_end=170,
  methods=[
  _descriptor.MethodDescriptor(
    name='RequestLoan',
    full_name='Borrow.RequestLoan',
    index=0,
    containing_service=None,
    input_type=_BORROWERREQUEST,
    output_type=_BORROWERRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_BORROW)

DESCRIPTOR.services_by_name['Borrow'] = _BORROW

# @@protoc_insertion_point(module_scope)