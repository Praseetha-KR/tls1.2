from construct import Embedded, Struct
from .common import record_layer, handshake_protocol
from .handshake_types import server_certificate as handshake_server_certificate


server_certificate_format = Struct(
    Embedded(record_layer),
    "handshake_protocol" / Struct(
        Embedded(handshake_protocol),
        Embedded(handshake_server_certificate),
    ),
)
