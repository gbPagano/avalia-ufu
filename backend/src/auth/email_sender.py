import smtplib
import ssl

from email.message import EmailMessage

from .token import create_access_token, ACCESS_TOKEN_EXPIRE_MINUTES
from .crypto import simetric_encrypt

MAIN_URL = "http://localhost:8000"
EMAIL = "avaliaufu@gmail.com"
EMAIL_PASSWORD = "ekmdylpytpahvmrb"


def send_confirmation_email(email_target: str):
    token = create_access_token(
        data={"sub": email_target}, minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )
    tgt = simetric_encrypt(email_target)
    msg = EmailMessage() 
    msg["Subject"] = "Confirmação de cadastro - App Wiki UFU"
    msg["From"] = "Avalia UFU"
    msg["To"] = "guilhermebpagano@gmail.com"
    msg.set_content(
        f"""
        Click no link abaixo para validar a sua conta:
        {MAIN_URL}/confirm-account/{token}?tgt={tgt}
        """,
    )

    with smtplib.SMTP_SSL(
        "smtp.gmail.com", 465, context=ssl.create_default_context()
    ) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
