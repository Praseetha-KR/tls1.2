import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import ec
from .cipher_suites import (
    CipherSuiteEnum, ECSupportedGroupEnum, SignatureHashAlgorithms
)


def gen_priv_key_obj(named_curve):
    if named_curve == 'secp256r1':
        return ec.generate_private_key(ec.SECP256R1(), default_backend())
    return None


def get_pub_key_hex(private_key):
    public_key = private_key.public_key()
    return public_key.public_numbers().encode_point()


def get_ip(hostname):
    try:
        ip = socket.gethostbyname(hostname)
        print('IP: {}'.format(ip))
        return ip
    except socket.gaierror as err:
        print('Couldn\'t resolve host IP. {}'.format(err))
        return None


def send_sock_msg(sock, msg):
    sock.sendall(msg)
    response = b''
    while True:
        result = sock.recv(1024)
        print('Recieved chunk of size {}...'.format(len(result)))
        response += result
        if not result:
            print('End of response.')
            break
    # print(response)
    return response


def get_ciphersuite(server_hello):
    return CipherSuiteEnum.get_key(
        server_hello.handshake_protocol.cipher_suite
    )


def get_signature_hash_algo(server_keyexchange):
    ec_dh = server_keyexchange.handshake_protocol.ec_dh_server_params
    return SignatureHashAlgorithms.get_key(
        ec_dh.signature_algorithm.hash, ec_dh.signature_algorithm.signature
    )


def get_signature(server_keyexchange):
    return server_keyexchange.handshake_protocol.ec_dh_server_params.signature


def get_ec_curve(server_keyexchange):
    ec_dh = server_keyexchange.handshake_protocol.ec_dh_server_params
    return ECSupportedGroupEnum.get_key(ec_dh.named_curve)


def get_peer_pubkey(server_keyexchange):
    return server_keyexchange.handshake_protocol.ec_dh_server_params.pubkey
