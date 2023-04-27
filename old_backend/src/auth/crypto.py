from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError


def encrypt(password: str) -> str:
    """Receives a password in plain text and returns a hash      

    Args:
        password (str): password get from user input

    Returns:
        str: hash to be stored in database
    """
    ph = PasswordHasher()
    hash = ph.hash(password)
    db_hash = hash[31:]

    return db_hash


def decrypt(db_hash: str, password: str) -> bool:
    """Receives a hash and a password in plain text, 
    and attempts to decrypt the hash with the password

    Args:
        db_hash (str): hash stored in database
        password (str): password get from user input

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
