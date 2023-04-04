from email.message import EmailMessage
import smtplib, ssl


MAIN_URL = "http://localhost:8000"
EMAIL = "avaliaufu@gmail.com"
EMAIL_PASSWORD = "ekmdylpytpahvmrb"


def send_confirmation_email(token: str, email_target: str):

    msg = EmailMessage()

    msg['Subject'] = f'Confirmação de cadastro - App Wiki UFU'
    msg['From'] = "Avalia UFU" 
    msg['To'] = email_target
    msg.set_content(f"""
        Click no link abaixo para validar a sua conta:
        {MAIN_URL}/user/confirm-account/{token}?validate_email={email_target}
        """,
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=ssl.create_default_context()) as server:
        server.login(EMAIL, EMAIL_PASSWORD)
        server.send_message(msg)
