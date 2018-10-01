from construct import Embedded, Struct
from .common import record_layer, handshake_protocol
from .handshake_types import (
    client_key_exchange as handshake_client_key_exchange
)


client_key_exchange_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Struct(
        Embedded(handshake_protocol),
        Embedded(handshake_client_key_exchange),
    ),
)
