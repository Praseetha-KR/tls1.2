from construct import (
    Byte, Bytes, Int8ub, Int16ub, Int24ub, Int32ub, Struct
)


protocol_version = Struct(
    "major" / Int8ub,
    "minor" / Int8ub
)

random = Struct(
    "gmt_unix_time" / Int32ub,
    "random_bytes" / Bytes(28)
)

extension_renegotiation_info = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "renegotiation_info_extension_length" / Int8ub
)
extension_server_name = Struct(
    "type" / Int16ub,
    "length" / Int16ub
)
extension_ec_point_formats = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "ec_point_formats_length" / Int8ub,
    "ec_point_formats" / Byte[3]
)
extension_alpn = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "alpn_extension_length" / Int16ub,
    "alpn_string_length" / Int8ub,
    "alpn_next_protocol" / Bytes(2)
)


server_hello_format = Struct(
    "record_content_type" / Int8ub,
    "record_version" / protocol_version,
    "record_length" / Int16ub,
    "handshake_type" / Int8ub,
    "length" / Int24ub,
    "version" / protocol_version,
    "random" / random,
    "session_id_length" / Int8ub,
    "session_id" / Bytes(32),
    "cipher_suite" / Int16ub,
    "compression_method" / Int8ub,
    "extensions_length" / Int16ub,

    "extension_renegotiation_info" / extension_renegotiation_info,
    "extension_server_name" / extension_server_name,
    "extension_ec_point_formats" / extension_ec_point_formats,
    "extension_alpn" / extension_alpn
)
