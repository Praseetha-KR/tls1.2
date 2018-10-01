from construct import Bytes, Int24ub, Struct, this


server_certificate = Struct(
    "certificates_length" / Int24ub,
    "certificates" / Bytes(this.certificates_length),
)
