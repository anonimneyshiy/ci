import hashlib


def get_password_hash(password: str) -> str:
    return hashlib.