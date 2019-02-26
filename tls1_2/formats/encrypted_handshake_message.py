from construct import Bytes, Embedded, Struct, this
from .common import record_layer


encrypted_handshake_message_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Bytes(this.record_length),
)
