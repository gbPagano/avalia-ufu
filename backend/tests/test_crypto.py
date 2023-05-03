import pytest

from src.auth.crypto import decrypt, encrypt, symmetric_decrypt, symmetric_encrypt


def test_same_target_returns_differents_hashes():
    hash_1 = encrypt("password")
    hash_2 = encrypt("password")

    assert hash_1 != hash_2


def test_correct_decrypt_returns_true():
    hash = encrypt("password")

    assert decrypt(hash, "password")


def test_wrong_decrypt_returns_false():
    hash = encrypt("password")

    assert not decrypt(hash, "wrong")


def test_same_target_returns_differents_symmetric_hashes():
    hash_1 = symmetric_encrypt("target")
    hash_2 = symmetric_encrypt("target")

    assert hash_1 != hash_2


def test_correct_symmetric_decrypt_returns_the_expected_text():
    hash = symmetric_encrypt("target")

    assert symmetric_decrypt(hash) == "target"


def test_wrong_symmetric_decrypt_raises_error():
    with pytest.raises(Exception):
        symmetric_decrypt("wrong")

