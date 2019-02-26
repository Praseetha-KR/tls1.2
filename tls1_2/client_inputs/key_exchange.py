from ..formats import client_key_exchange_format


def client_key_exchange(pubkey):
    return client_key_exchange_format.build({
        "record_content_type": 22,
        "record_version": {
            "major": 0x03,
            "minor": 0x03
        },
        "record_length": 70,
        "handshake_protocol": {
            "handshake_type": 16,
            "length": len(pubkey) + 1,
            "ec_dh_client_params": {
                "pubkey_length": len(pubkey),
                "pubkey": pubkey
            }
        }
    })
