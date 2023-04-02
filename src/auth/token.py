from datetime import timedelta
from fastapi_login import LoginManager


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





