import hashlib


def md5(raw: str) -> str:
    m = hashlib.md5()
    m.update(raw.encode(encoding='utf-8'))
    psw = m.hexdigest()
    return psw
