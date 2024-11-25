from pydantic_settings import BaseSettings
from pydantic import (
    BaseModel,
    PostgresDsn,
)


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 8000


class APIPrefixConfig(BaseModel):
    prefix: str = '/api'


class DatabaseConfig(BaseModel):
    url: PostgresDsn
    echo: bool = False
    echo_pool: bool = False
    pool_size: int = 50
    max_overflow: int = 10


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIPrefixConfig = APIPrefixConfig()
    db: DatabaseConfig


settings = Settings()
