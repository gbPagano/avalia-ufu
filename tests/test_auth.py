from src.auth.crypto import decrypt, encrypt


def test_same_passwords_returns_differents_hashes():
    hash_1 = encrypt("password")
    hash_2 = encrypt("password")

    assert hash_1 != hash_2


def test_correct_decrypt_returns_true():
    hash = encrypt("password")

    assert decrypt(hash, "password")


def test_wrong_decrypt_returns_false():
    hash = encrypt("password")

    assert not decrypt(hash, "wrong")
