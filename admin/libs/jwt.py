import jwt
import os


def jwt_encode(payload: dict, headers: dict) -> str:
    try:
        current_dir = os.getcwd()
        with open('rsa_private_key.pem', 'r') as fh:
            signing_key = fh.read()
    except Exception as error:
        raise error
    compact_jws = jwt.encode(payload, signing_key, 'RS256', headers=headers).decode(encoding="UTF-8")
    return compact_jws


def jwt_decode(compact_jws: str) -> dict:
    with open('rsa_public_key.pem', 'rb') as fh:
        verifying_key = fh.read()
    try:
        payload = jwt.decode(compact_jws, verifying_key, 'RS256')
    except Exception as err:
        raise err
    return payload
