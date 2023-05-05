from pathlib import Path

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.database.core import Base, get_db
from src.auth.email_sender import send_confirmation_email
from src.main import app


db_test = Path() / "tests/test.db"
if db_test.exists():
    db_test.unlink()


SQLALCHEMY_DATABASE_URL = "sqlite:///./tests/test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)


def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"hello": "world"}


def test_invalid_register_user():
    response = client.post(
        "/register",
        json={
            "name": "testinho",
            "email": "test@email.com",
            "registration": "12111EEL000",
            "password": "senha123",
        },
    )
    assert response.status_code == 422, response.text
    assert "it's not an email from ufu" in response.text


def test_register_user():
    response = client.post(
        "/register",
        json={
            "name": "testinho",
            "email": "test@ufu.br",
            "registration": "12111EEL000",
            "password": "senha123",
        },
    )
    assert response.status_code == 201, response.text
    data = response.json()
    assert data["role"] == "user", response.text
    assert not data["is_confirmed"], response.text


def test_already_register_user():
    response = client.post(
        "/register",
        json={
            "name": "testinho",
            "email": "test@ufu.br",
            "registration": "12111EEL000",
            "password": "senha123",
        },
    )
    assert response.status_code == 400, response.text
    assert "User already registered" in response.text


def test_get_me_works():
    response = client.get("/me")
    assert response.status_code == 200, response.text


def test_logout():
    response = client.post("/logout")
    assert response.status_code == 200


def test_get_me_fails():
    response = client.get("/me")
    assert response.status_code == 401, response.text


def test_wrong_login():
    response = client.post(
        "/login",
        headers={
            'Content-Type': 'application/x-www-form-urlencoded', 
            'accept': 'application/json'
        },
        data={
            "username": "test@ufu.br",
            "password": "wrong",
        },
    )
    assert response.status_code == 401, response.text


def test_correct_login():
    response = client.post(
        "/login",
        headers={
            'Content-Type': 'application/x-www-form-urlencoded', 
            'accept': 'application/json'
        },
        data={
            "username": "test@ufu.br",
            "password": "senha123",
        },
    )
    data = response.json()
    assert response.status_code == 200, response.text
    assert data["name"] == "testinho", response.text


def test_confirm_account():
    url = send_confirmation_email("test@ufu.br")
    response = client.get(url)
    data = response.json()
    assert response.status_code == 200, response.text
    assert data["is_confirmed"], response.text

