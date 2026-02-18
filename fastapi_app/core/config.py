from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"
    DB_URL: str = "postgresql+asyncpg://grin:grin@localhost:5432/grin"
    DB_ECHO: bool = True


settings = Settings()
