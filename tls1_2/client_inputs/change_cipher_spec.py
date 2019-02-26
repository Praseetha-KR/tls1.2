from ..formats import change_cipher_spec_format


def client_change_cipher_spec():
    return change_cipher_spec_format.build({
        "record_content_type": 20,
        "record_version": {
            "major": 0x03,
            "minor": 0x03
        },
        "record_length": 1,
        "change_cipher_spec_message": 1,
    })
