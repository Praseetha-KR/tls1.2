from construct import Byte, Bytes, Int8ub, Int16ub, Struct
from ..common import protocol_version, random


# Extensions
extension_renegotiation_info = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "renegotiation_info_extension_length" / Int8ub,
)
extension_server_name = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
)
extension_ec_point_formats = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "ec_point_formats_length" / Int8ub,
    "ec_point_formats" / Byte[3],
)
extension_alpn = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "alpn_extension_length" / Int16ub,
    "alpn_string_length" / Int8ub,
    "alpn_next_protocol" / Bytes(2),
)


server_hello = Struct(
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
    "extension_alpn" / extension_alpn,
)
