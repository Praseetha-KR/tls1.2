import socket
import hashlib
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.kdf.hkdf import HKDF
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from tls1_2.client_inputs import (
    client_hello, client_key_exchange, client_change_cipher_spec,
    client_encrypted_handshake_message
)
from tls1_2.parsers import HelloResponseParser
import tls1_2.utils as utils


# Connect
ip = utils.get_ip(b'imagineer.in')
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, 443))

# Client Hello, Server Hello, Certificate, Server Key Exchange
response = utils.send_sock_msg(s, client_hello())

# (
#     server_hello,
#     server_certificate,
#     server_key_exchange,
#     server_hello_done
# ) = utils.parse_client_response(response)

msgs = HelloResponseParser(response).parse()

ciphersuite = utils.get_ciphersuite(msgs.server_hello.msg_struct)
sign_hash_algo = utils.get_signature_hash_algo(
    msgs.server_key_exchange.msg_struct
)
signature = utils.get_signature(msgs.server_key_exchange.msg_struct)
curve = utils.get_ec_curve(msgs.server_key_exchange.msg_struct)
peer_pubkey = utils.get_peer_pubkey(msgs.server_key_exchange.msg_struct)
print(ciphersuite, sign_hash_algo, curve, peer_pubkey)

ecpubnums = ec.EllipticCurvePublicNumbers.from_encoded_point(
    curve=ec.SECP256R1(), data=peer_pubkey
)
server_public_key = ecpubnums.public_key(backend=default_backend())

privkey_obj = utils.gen_priv_key_obj(curve)
client_public_key = utils.get_pub_key_hex(privkey_obj)
# pubkey_obj = privkey_obj.public_key()
# public_key = privkey_obj.public_numbers().encode_point()

shared_key = privkey_obj.exchange(ec.ECDH(), server_public_key)
pre_master_secret = shared_key

data_exchanged = (
    client_hello()[5:] +
    msgs.server_hello.msg_bytes[5:] +
    msgs.server_certificate.msg_bytes[5:] +
    msgs.server_key_exchange.msg_bytes[5:] +
    msgs.server_hello_done.msg_bytes[5:] +
    client_key_exchange(client_public_key)[5:] +
    client_change_cipher_spec()[5:]
)
message = hashlib.sha256(data_exchanged).digest()
# data_hash = PRF(shared_secret, "client finished", hash, 12)

derived_key = HKDF(
    algorithm=hashes.SHA256(),
    length=32,
    salt=os.urandom(12),
    info=b'client finished',
    backend=default_backend()
).derive(shared_key)

# aesgcm_key = AESGCM.generate_key(bit_length=128)
aesgcm = AESGCM(shared_key)
nonce = os.urandom(12)
encrypted_data = aesgcm.encrypt(
    nonce, b'\x14\x00\x00\x0C' + message, None
)
# print(b'\x14\x00\x00\x0C' + data_hash)
# print(aesgcm.decrypt(os.urandom(12), encrypted_data, None))
cliex = (
    client_key_exchange(client_public_key) +
    client_change_cipher_spec() +
    client_encrypted_handshake_message(encrypted_data)
)

cliex_response = utils.send_sock_msg(s, cliex)
print(cliex_response)

# s.close()
