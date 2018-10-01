def hexsplit(hexnum):
    return list(divmod(hexnum, 0x100))


def format_sign_hash(value):
    [hash, signature] = hexsplit(value)
    return {
        "hash": hash,
        "signature": signature,
    }
