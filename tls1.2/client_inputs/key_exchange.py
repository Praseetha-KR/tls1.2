from formats import client_key_exchange_format


client_key_exchange = client_key_exchange_format.build({
    "record_content_type": 22,
    "record_version": {
        "major": 0x03,
        "minor": 0x03
    },
    "record_length": 70,
    "handshake_protocol": {
        "handshake_type": 16,
        "length": 66,
        "ec_dh_client_params": {
            "pubkey_length": 65,
            "pubkey": b'\x04\x57\xe3\xcc\xec\x8b\x5d\xfe\x25\x95\x6f\xa5\xff\x1f\x2d\x02\xa3\x2f\x5c\x4c\xf7\xba\x47\xcb\xde\x70\x9e\x6a\xfd\x9b\xd1\xb4\xd1\xe9\xf2\x4d\x7f\x27\x40\x24\xa9\x16\x89\x08\x57\x7a\x4c\x23\x0a\xa1\x67\x2a\x79\x18\xe7\xf2\x55\x91\x49\x81\x06\x44\x6e\xc4\x66'  # noqa
        }
    }
})
