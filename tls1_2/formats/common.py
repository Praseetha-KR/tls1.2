from construct import Bytes, Int8ub, Int16ub, Int24ub, Int32ub, Struct


protocol_version = Struct(
    "major" / Int8ub,
    "minor" / Int8ub,
)

random = Struct(
    "gmt_unix_time" / Int32ub,
    "random_bytes" / Bytes(28)
)

record_layer = Struct(
    "record_content_type" / Int8ub,
    "record_version" / protocol_version,
    "record_length" / Int16ub,
)

handshake_protocol = Struct(
    "handshake_type" / Int8ub,
    "length" / Int24ub,
)
