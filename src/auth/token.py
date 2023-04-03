from datetime import timedelta

from fastapi_login import LoginManager
from email.message import EmailMessage
import smtplib, ssl
from fastapi.requests import Request
from fastapi.responses import RedirectResponse


MAIN_URL = "http://localhost:8000"
EMAIL = "avaliaufu@gmail.com"
EMAIL_PASSWORD = "jpotofxfskaysung"
SECRET = "super-secret-key"



class NotAuthenticatedException(Exception):
    pass

manager = LoginManager(
    SECRET, 
    '/login', 
    use_cookie=True,
    use_header=False, 
    default_expiry=timedelta(hours=12),
    custom_exception=NotAuthenticatedException
)

def auth_exception_handler(request: Request, exc: NotAuthenticatedException):
    """
    Redirect the user to the login page if n eot logged in
    """
    return RedirectResponse(url='/login')


def send_confirmation_email(token: str, email_target: str):

    msg = EmailMessage()

    msg['Subject'] = f'Confirmação de cadastro - App Wiki UFU'
    msg['From'] = EMAIL
    msg['To'] = email_target
    msg.set_content(f"""
        Click no link abaixo para validar a sua conta:
        {MAIN_URL}/user/confirm-account/{token}?validate_email={email_target}
        """,
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)


