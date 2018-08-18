import json
from jwt import JWT, jwk_from_pem

jwt = JWT()


def get_token(message: dict) -> str:
    with open('rsa_private_key.pem', 'rb') as fh:
        signing_key = jwk_from_pem(fh.read())
    compact_jws = jwt.encode(message, signing_key, 'RS256')
    return compact_jws


def verify_token(compact_jws: str)->dict:
    with open('rsa_public_key.pem', 'rb') as fh:
        verifying_key = jwk_from_pem(fh.read())
    try:
        message = jwt.decode(compact_jws, verifying_key, 'RS256')
    except Exception as err:
        raise err
    return message
