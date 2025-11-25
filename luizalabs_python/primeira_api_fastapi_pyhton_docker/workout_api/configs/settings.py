from pydantic import Field
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DB_URL: str = Field(
        default="postgresql+asyncpg://postgres:nd4/3/97@localhost/postgres"
    )


settings = Settings()
