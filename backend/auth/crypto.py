from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from cryptography.fernet import Fernet, InvalidToken

from .exceptions import InvalidCredentialsException
from .token import SECRET_KEY


def encrypt(password: str) -> str:
    """Receives a password in plain text and returns a hash.

    Args:
        password: password get from user input

    Returns:
        str: hash to be stored in database
    """
    ph = PasswordHasher()
    hash = ph.hash(password)
    db_hash = hash[31:]

    return db_hash


def decrypt(db_hash: str, password: str) -> bool:
    """Receives a hash and a password in plain text,
    and attempts to decrypt the hash with the password.

    Args:
        db_hash: hash stored in database
        password: password get from user input

    Returns:
        bool: true if the password is correct
    """
    base = "$argon2id$v=19$m=65536,t=3,p=4$"
    ph = PasswordHasher()
    try:
        ph.verify(base + db_hash, password)
        return True
    except VerifyMismatchError:
        return False


def symmetric_encrypt(target: str) -> str:
    """Receives a target in plain text and returns a symmetric hash

    Args:
        target: text to be hashed

    Returns:
        str: symmetric hash
    """
    return Fernet(SECRET_KEY).encrypt(target.encode()).decode()


def symmetric_decrypt(target: str) -> str:
    """Receives a symmetric hash in plain text,
    and attempts to decrypt the hash.

    Args:
        target: hash to be decrypted

    Returns:
        str: the decrypted text
    """
    try:
        return Fernet(SECRET_KEY).decrypt(target).decode()
    except InvalidToken:
        raise InvalidCredentialsException
