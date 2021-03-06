# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: libreasr.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


DESCRIPTOR = _descriptor.FileDescriptor(
    name="libreasr.proto",
    package="ASR",
    syntax="proto3",
    serialized_options=None,
    serialized_pb=b'\n\x0elibreasr.proto\x12\x03\x41SR"!\n\x05\x41udio\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\n\n\x02sr\x18\x03 \x01(\x05"\x1a\n\nTranscript\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\t2i\n\x03\x41SR\x12+\n\nTranscribe\x12\n.ASR.Audio\x1a\x0f.ASR.Transcript"\x00\x12\x35\n\x10TranscribeStream\x12\n.ASR.Audio\x1a\x0f.ASR.Transcript"\x00(\x01\x30\x01\x62\x06proto3',
)


_AUDIO = _descriptor.Descriptor(
    name="Audio",
    full_name="ASR.Audio",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="ASR.Audio.data",
            index=0,
            number=1,
            type=12,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"",
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
        _descriptor.FieldDescriptor(
            name="sr",
            full_name="ASR.Audio.sr",
            index=1,
            number=3,
            type=5,
            cpp_type=1,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=23,
    serialized_end=56,
)


_TRANSCRIPT = _descriptor.Descriptor(
    name="Transcript",
    full_name="ASR.Transcript",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    fields=[
        _descriptor.FieldDescriptor(
            name="data",
            full_name="ASR.Transcript.data",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=58,
    serialized_end=84,
)

DESCRIPTOR.message_types_by_name["Audio"] = _AUDIO
DESCRIPTOR.message_types_by_name["Transcript"] = _TRANSCRIPT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Audio = _reflection.GeneratedProtocolMessageType(
    "Audio",
    (_message.Message,),
    {
        "DESCRIPTOR": _AUDIO,
        "__module__": "libreasr_pb2"
        # @@protoc_insertion_point(class_scope:ASR.Audio)
    },
)
_sym_db.RegisterMessage(Audio)

Transcript = _reflection.GeneratedProtocolMessageType(
    "Transcript",
    (_message.Message,),
    {
        "DESCRIPTOR": _TRANSCRIPT,
        "__module__": "libreasr_pb2"
        # @@protoc_insertion_point(class_scope:ASR.Transcript)
    },
)
_sym_db.RegisterMessage(Transcript)


_ASR = _descriptor.ServiceDescriptor(
    name="ASR",
    full_name="ASR.ASR",
    file=DESCRIPTOR,
    index=0,
    serialized_options=None,
    serialized_start=86,
    serialized_end=191,
    methods=[
        _descriptor.MethodDescriptor(
            name="Transcribe",
            full_name="ASR.ASR.Transcribe",
            index=0,
            containing_service=None,
            input_type=_AUDIO,
            output_type=_TRANSCRIPT,
            serialized_options=None,
        ),
        _descriptor.MethodDescriptor(
            name="TranscribeStream",
            full_name="ASR.ASR.TranscribeStream",
            index=1,
            containing_service=None,
            input_type=_AUDIO,
            output_type=_TRANSCRIPT,
            serialized_options=None,
        ),
    ],
)
_sym_db.RegisterServiceDescriptor(_ASR)

DESCRIPTOR.services_by_name["ASR"] = _ASR

# @@protoc_insertion_point(module_scope)
