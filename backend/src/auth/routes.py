from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.database import schemas, crud, core
from .token import send_confirmation_email

app_auth = APIRouter(
    prefix="",
    tags=["authentication"],
)


@app_auth.post("/register")
def register(
    user: schemas.UserCreate,
    db: Session = Depends(core.get_db),
):
    userdb_email = crud.get_user_by_email(email=user.email, db=db)
    userdb_registration = crud.get_user_by_registration(registration=user.registration, db=db)
    if userdb_email or userdb_registration:
        raise HTTPException(status_code=400, detail="User already registered")

    new_user = crud.create_user(user=user, db=db)

    send_confirmation_email("token", "guilhermebpagano@gmail.com")

    return new_user
