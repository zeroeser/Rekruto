from typing import Any, Dict, Optional

from pydantic import AnyUrl, BaseSettings, PostgresDsn, validator


class Settings(BaseSettings):
    API_PATH: str = ""
    PROJECT_NAME: str

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
