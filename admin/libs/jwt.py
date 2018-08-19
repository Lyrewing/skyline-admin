import jwt


def jwt_encode(payload: dict,headers:dict) -> str:
    with open('rsa_private_key.pem', 'rb') as fh:
        signing_key = fh.read()
    compact_jws = jwt.encode(payload,signing_key, 'RS256',headers=headers)
    return compact_jws


def jwt_decode(compact_jws: str)->dict:
    with open('rsa_public_key.pem', 'rb') as fh:
        verifying_key = fh.read()
    try:
        payload = jwt.decode(compact_jws, verifying_key, 'RS256')
    except Exception as err:
        raise err
    return payload
