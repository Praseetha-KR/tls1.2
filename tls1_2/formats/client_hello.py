from construct import Embedded, Struct
from .common import record_layer, handshake_protocol
from .handshake_types import client_hello as handshake_client_hello


client_hello_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Struct(
        Embedded(handshake_protocol),
        Embedded(handshake_client_hello),
    ),
)
