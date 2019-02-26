import os
import time

from ..consts import (
    SERVER_NAME, CLIENT_HELLO_PADDING_LEN, ALPN_PROTOCOL_1, ALPN_PROTOCOL_2,
    EXTN_META_LEN
)
from ..formats import client_hello_format
from ..cipher_suites import (
    CipherSuiteEnum, ECSupportedGroupEnum, SignatureHashAlgorithms
)


cipher_suites_count = len(CipherSuiteEnum)
ec_support_group_count = len(ECSupportedGroupEnum)
sign_hash_algo_count = len(SignatureHashAlgorithms)
server_name_len = len(SERVER_NAME)
alpn_1_len = len(ALPN_PROTOCOL_1)
alpn_2_len = len(ALPN_PROTOCOL_2)


def client_hello():
    return client_hello_format.build({
        "record_content_type": 22,
        "record_version": {
            "major": 0x03,
            "minor": 0x01
        },
        "record_length": 434,
        "handshake_protocol": {
            "handshake_type": 1,
            "length": 430,
            "version": {
                "major": 0x03,
                "minor": 0x03
            },
            "random": {
                "gmt_unix_time": int(time.time()),
                "random_bytes": os.urandom(28)
            },
            "session_id_length": 0,
            "cipher_suites_length": 2 * cipher_suites_count,
            "cipher_suites": CipherSuiteEnum.get_keys(),
            "compression_methods_length": 1,
            "compression_methods": 0,
            "extensions_length": (
                server_name_len + 5 + EXTN_META_LEN +
                4 + 4 +
                2 * ec_support_group_count + 2 + EXTN_META_LEN +
                2 * sign_hash_algo_count + 2 + 4 +
                0 + EXTN_META_LEN +
                alpn_1_len + alpn_2_len + 4 + EXTN_META_LEN +
                CLIENT_HELLO_PADDING_LEN + EXTN_META_LEN
            ),
            "extension_server_name": {
                "type": 0,
                "length": server_name_len + 5,
                "server_name_list_length": server_name_len + 3,
                "server_name_type": 0,
                "server_name_length": server_name_len,
                "server_name": SERVER_NAME
            },
            "extension_ec_point_formats": {
                "type": 11,
                "length": 4,
                "ec_point_formats_length": 3,
                "ec_point_formats": [0, 1, 2]
            },
            "extension_supported_groups": {
                "type": 10,
                "length": 2 * ec_support_group_count + 2,
                "supported_groups_list_length": 2 * ec_support_group_count,
                "supported_groups": ECSupportedGroupEnum.get_keys()
            },
            "extension_signature_algorithms": {
                "type": 13,
                "length": 2 * sign_hash_algo_count + 2,
                "signature_hash_algorithms_length": 2 * sign_hash_algo_count,
                "signature_hash_algorithms": SignatureHashAlgorithms.get_keys()
            },
            "extension_next_protocol_negotiation": {
                "type": 13172,
                "length": 0,
            },
            "extension_application_layer_protocol_negotiation": {
                "type": 16,
                "length": alpn_1_len + alpn_2_len + 4,
                "alpn_extension_length": (
                    alpn_1_len + alpn_2_len + 2
                ),
                "alpn_string_length1": alpn_1_len,
                "alpn_next_protocol1": ALPN_PROTOCOL_1,
                "alpn_string_length2": alpn_2_len,
                "alpn_next_protocol2": ALPN_PROTOCOL_2,
            },
            "extension_padding": {
                "type": 21,
                "length": CLIENT_HELLO_PADDING_LEN,
                "padding_data": b'\x00'*CLIENT_HELLO_PADDING_LEN
            },
        }
    })
