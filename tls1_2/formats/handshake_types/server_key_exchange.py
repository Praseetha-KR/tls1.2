from construct import Bytes, Int8ub, Int16ub, Struct, this

signature_hash_algorithm = Struct(
    "hash" / Int8ub,
    "signature" / Int8ub
)

ec_dh_server_params = Struct(
    "curve_type" / Int8ub,
    "named_curve" / Int16ub,
    "pubkey_length" / Int8ub,
    "pubkey" / Bytes(this.pubkey_length),
    "signature_algorithm" / signature_hash_algorithm,
    "signature_length" / Int16ub,
    "signature" / Bytes(this.signature_length),
)

server_key_exchange = Struct(
    "ec_dh_server_params" / ec_dh_server_params,
)
