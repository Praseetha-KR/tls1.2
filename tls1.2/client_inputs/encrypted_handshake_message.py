from formats import encrypted_handshake_message_format


client_encrypted_handshake_message = encrypted_handshake_message_format.build({
    "record_content_type": 22,
    "record_version": {
        "major": 0x03,
        "minor": 0x03
    },
    "record_length": 40,
    "handshake_protocol": b'\x00\x00\x00\x00\x00\x00\x00\x00\xb6\x79\x73\xc8\xdf\x84\x32\x9a\xb3\x22\xa0\xe3\x90\xce\x07\x3a\xe1\xd3\x78\x7d\x5d\x29\x0b\x2e\xb4\xac\x9c\xb5\x88\x7a\x52\x98'  # noqa
})
