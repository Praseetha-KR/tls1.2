from enum import Enum


def hexsplit(hexnum):
    return list(divmod(hexnum, 0x100))


class CipherSuiteEnum(Enum):
    TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256 = 0xcc14
    TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 = 0xc02b
    TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 = 0xc02c
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA256 = 0xc023
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA384 = 0xc024
    TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA = 0xc009
    TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA = 0xc00a
    TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256 = 0xcc13
    TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 = 0xc02f
    TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 = 0xc030
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256 = 0xc027
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384 = 0xc028
    TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA = 0xc013
    TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA = 0xc014
    TLS_DHE_RSA_WITH_CHACHA20_POLY1305_SHA256 = 0xcc15
    TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 = 0x009f
    TLS_DHE_RSA_WITH_AES_128_GCM_SHA256 = 0x009e
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA256 = 0x006b
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA256 = 0x0067
    TLS_DHE_RSA_WITH_AES_256_CBC_SHA = 0x0039
    TLS_DHE_RSA_WITH_AES_128_CBC_SHA = 0x0033
    TLS_RSA_WITH_AES_256_GCM_SHA384 = 0x009d
    TLS_RSA_WITH_AES_128_GCM_SHA256 = 0x009c
    TLS_RSA_WITH_AES_128_CBC_SHA256 = 0x003c
    TLS_RSA_WITH_AES_256_CBC_SHA256 = 0x003d
    TLS_RSA_WITH_AES_128_CBC_SHA = 0x002f
    TLS_RSA_WITH_AES_256_CBC_SHA = 0x0035
    TLS_EMPTY_RENEGOTIATION_INFO_SCSV = 0x00ff

    @classmethod
    def get_keys(cls):
        return [hexsplit(x.value) for x in cls]

    @classmethod
    def get_key(cls, value):
        for e in cls:
            if e.value == value:
                return e.name
        return None


class ECSupportedGroupEnum(Enum):
    brainpoolP512r1 = 0x001c
    brainpoolP384r1 = 0x001b
    brainpoolP256r1 = 0x001a
    secp521r1 = 0x0019
    secp384r1 = 0x0018
    secp256r1 = 0x0017
    secp256k1 = 0x0016
    secp224r1 = 0x0015
    secp224k1 = 0x0014
    secp192r1 = 0x0013
    secp192k1 = 0x0012
    secp160r2 = 0x0011
    secp160r1 = 0x0010
    secp160k1 = 0x000f
    sect571r1 = 0x000e
    sect571k1 = 0x000d
    sect409r1 = 0x000c
    sect409k1 = 0x000b
    sect283r1 = 0x000a
    sect283k1 = 0x0009
    sect239k1 = 0x0008
    sect233r1 = 0x0007
    sect233k1 = 0x0006
    sect193r2 = 0x0005
    sect193r1 = 0x0004
    sect163r2 = 0x0003
    sect163r1 = 0x0002
    sect163k1 = 0x0001

    @classmethod
    def get_keys(cls):
        return [hexsplit(x.value) for x in cls]

    @classmethod
    def get_key(cls, value):
        for e in cls:
            if e.value == value:
                return e.name
        return None


class SignatureHashAlgorithms(Enum):
    ecdsa_secp521r1_sha512 = 0x0603
    SHA512_DSA = 0x0602
    rsa_pkcs1_sha512 = 0x0601
    ecdsa_secp384r1_sha384 = 0x0503
    SHA384_DSA = 0x0502
    rsa_pkcs1_sha384 = 0x0501
    ecdsa_secp256r1_sha256 = 0x0403
    SHA256_DSA = 0x0402
    rsa_pkcs1_sha256 = 0x0401
    SHA224_ECDSA = 0x0303
    SHA224_DSA = 0x0302
    SHA224_RSA = 0x0301
    ecdsa_sha1 = 0x0203
    SHA1_DSA = 0x0202
    rsa_pkcs1_sha1 = 0x0201

    @classmethod
    def to_sign_hash(cls, value):
        [hash, signature] = hexsplit(value)
        return {
            "hash": hash,
            "signature": signature,
        }

    @classmethod
    def get_keys(cls):
        return [cls.to_sign_hash(x.value) for x in cls]

    @classmethod
    def get_key(cls, hash, sign):
        value = hash * 0x100 + sign
        for e in cls:
            if e.value == value:
                return e.name
        return None
