from fastapi import HTTPException, status

InvalidCredentialsException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Invalid credentials",
)

ExpiredTokenException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Token has expired",
)

UnconfirmedAccountException = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Unconfirmed account",
)
