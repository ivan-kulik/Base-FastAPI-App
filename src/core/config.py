from pydantic_settings import BaseSettings
from pydantic import BaseModel


class RunConfig(BaseModel):
    host: str = 'localhost'
    port: int = 8000


class APIPrefixConfig(BaseModel):
    prefix: str = '/api'


class Settings(BaseSettings):
    run: RunConfig = RunConfig()
    api: APIPrefixConfig = APIPrefixConfig()


settings = Settings()
