from datetime import datetime, timedelta, timezone

from jose import JWTError, jwt

from fastapi_app.core.config import settings


def create_access_token(*, user_id: int) -> str:
    now = datetime.now(timezone.utc)
    payload = {
        "sub": str(user_id),
        "iat": int(now.timestamp()),
        "exp": int((now + timedelta(minutes=settings.JWT_EXPIRES_MINUTES)).timestamp()),
    }
    return jwt.encode(payload, settings.JWT_SECRET, algorithm=settings.JWT_ALGORITHM)


def decode_access_token(token: str) -> int:
    try:
        payload = jwt.decode(
            token,
            settings.JWT_SECRET,
            algorithms=[settings.JWT_ALGORITHM],
        )
    except JWTError as exc:
        raise ValueError("Invalid token") from exc

    sub = payload.get("sub")
    if not sub:
        raise ValueError("Token missing subject")

    try:
        return int(sub)
    except (TypeError, ValueError) as exc:
        raise ValueError("Invalid subject") from exc

