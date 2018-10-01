from construct import Bytes, Embedded, Struct, this
from .common import record_layer


change_cipher_spec_format = Struct(
    Embedded(record_layer),
    "change_cipher_spec_message" / Bytes(this.record_length)
)
