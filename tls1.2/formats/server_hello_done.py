from construct import Embedded, Struct
from .common import record_layer, handshake_protocol


server_hello_done_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Struct(
        Embedded(handshake_protocol),
    ),
)
