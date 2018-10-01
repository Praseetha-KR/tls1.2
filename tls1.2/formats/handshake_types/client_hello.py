from construct import Byte, Bytes, Int8ub, Int16ub, Struct, this
from ..common import protocol_version, random


cipher_suite = Byte[2]
support_group = Byte[2]
signature_algorithm = Struct(
    "hash" / Int8ub,
    "signature" / Int8ub,
)

# Extensions
extension_server_name = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "server_name_list_length" / Int16ub,
    "server_name_type" / Int8ub,
    "server_name_length" / Int16ub,
    "server_name" / Bytes(this.server_name_length)
)
extension_ec_point_formats = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "ec_point_formats_length" / Int8ub,
    "ec_point_formats" / Byte[3]
)
extension_supported_groups = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "supported_groups_list_length" / Int16ub,
    "supported_groups" / support_group[this.supported_groups_list_length / 2]
)
extension_signature_algorithms = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "signature_hash_algorithms_length" / Int16ub,
    "signature_hash_algorithms" / signature_algorithm[
        this.signature_hash_algorithms_length / 2
    ],
)
extension_next_protocol_negotiation = Struct(
    "type" / Int16ub,
    "length" / Int16ub
)
extension_application_layer_protocol_negotiation = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "alpn_extension_length" / Int16ub,
    "alpn_string_length1" / Int8ub,
    "alpn_next_protocol1" / Bytes(this.alpn_string_length1),
    "alpn_string_length2" / Int8ub,
    "alpn_next_protocol2" / Bytes(this.alpn_string_length2),
)
extension_padding = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "padding_data" / Bytes(this.length),
)


client_hello = Struct(
    "version" / protocol_version,
    "random" / random,
    "session_id_length" / Int8ub,
    "cipher_suites_length" / Int16ub,
    "cipher_suites" / cipher_suite[this.cipher_suites_length / 2],
    "compression_methods_length" / Int8ub,
    "compression_methods" / Int8ub,
    "extensions_length" / Int16ub,
    "extension_server_name" / extension_server_name,
    "extension_ec_point_formats" / extension_ec_point_formats,
    "extension_supported_groups" / extension_supported_groups,
    "extension_signature_algorithms" / extension_signature_algorithms,
    "extension_next_protocol_negotiation" / (
        extension_next_protocol_negotiation
    ),
    "extension_application_layer_protocol_negotiation" / (
        extension_application_layer_protocol_negotiation
    ),
    "extension_padding" / extension_padding,
)
