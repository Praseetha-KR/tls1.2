from construct import Embedded, Struct
from .common import record_layer, handshake_protocol
from .handshake_types import (
    server_key_exchange as handshake_server_key_exchange
)


server_key_exchange_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Struct(
        Embedded(handshake_protocol),
        Embedded(handshake_server_key_exchange),
    ),
)
