from construct import (
    Byte, Bytes, Int8ub, Int16ub, Int24ub, Int32ub, Struct
)
from consts import (
    SERVER_NAME, CLIENT_HELLO_PADDING_LEN, ALPN_PROTOCOL_1, ALPN_PROTOCOL_2
)
from cipher_suites import (
    CipherSuiteEnum, ECSupportedGroupEnum, SignatureHashAlgorithms
)


protocol_version = Struct(
    "major" / Int8ub,
    "minor" / Int8ub
)
random = Struct(
    "gmt_unix_time" / Int32ub,
    "random_bytes" / Bytes(28)
)
cipher_suite = Byte[2]
support_group = Byte[2]
sign_hash_algo = Byte[2]
extension_server_name = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "server_name_list_length" / Int16ub,
    "server_name_type" / Int8ub,
    "server_name_length" / Int16ub,
    "server_name" / Bytes(len(SERVER_NAME))
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
    "supported_groups" / support_group[len(ECSupportedGroupEnum)]
)
extension_signature_algorithms = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "signature_hash_algorithms_length" / Int16ub,
    "signature_hash_algorithms" / sign_hash_algo[len(SignatureHashAlgorithms)]
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
    "alpn_next_protocol1" / Bytes(len(ALPN_PROTOCOL_1)),
    "alpn_string_length2" / Int8ub,
    "alpn_next_protocol2" / Bytes(len(ALPN_PROTOCOL_2))
)
extension_padding = Struct(
    "type" / Int16ub,
    "length" / Int16ub,
    "padding_data" / Bytes(CLIENT_HELLO_PADDING_LEN)
)

client_hello_format = Struct(
    "record_content_type" / Int8ub,
    "record_version" / protocol_version,
    "record_length" / Int16ub,
    "handshake_type" / Int8ub,
    "length" / Int24ub,
    "version" / protocol_version,
    "random" / random,
    "session_id_length" / Int8ub,
    "cipher_suites_length" / Int16ub,
    "cipher_suites" / cipher_suite[len(CipherSuiteEnum)],
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
    "extension_padding" / extension_padding
)
