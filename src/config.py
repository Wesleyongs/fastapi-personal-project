from functools import lru_cache
from pydantic import BaseSettings


class Settings(BaseSettings):
    db_url = "postgresql://postgres:chickendinner@database-1.csacw5oszee1.ap-southeast-1.rds.amazonaws.com"

    class Config:
        env_prefix = "APP_"

@lru_cache()
def get_setting():
    return Settings()