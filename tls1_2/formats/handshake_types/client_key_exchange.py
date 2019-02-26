from construct import Bytes, Int8ub, Struct, this

ec_dh_client_params = Struct(
    "pubkey_length" / Int8ub,
    "pubkey" / Bytes(this.pubkey_length)
)

client_key_exchange = Struct(
    "ec_dh_client_params" / ec_dh_client_params
)
