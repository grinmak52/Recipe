from fastapi import APIRouter
from pydantic import BaseModel, Field

from fastapi_app.core.security import create_access_token

router = APIRouter(tags=["Auth"])


class TokenRequest(BaseModel):
    user_id: int = Field(gt=0)


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"


@router.post("/token", response_model=TokenResponse)
async def issue_token(payload: TokenRequest) -> TokenResponse:
    """
    Dev-only endpoint for portfolio/demo.
    In production replace with real authentication (password/JWT refresh/etc).
    """
    return TokenResponse(access_token=create_access_token(user_id=payload.user_id))

