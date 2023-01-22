from pathlib import Path

from pydantic import BaseSettings


class Settings(BaseSettings):

    ROOT_DIR: Path = Path(__file__).parents[1]

    API_HOST: str
    API_PORT: int
    API_LOG_LEVEL: str = "INFO"
    API_RELOAD: bool = False

    DB_FILE_NAME: str = "db.json"
    STORAGE_DIR: Path = ROOT_DIR / "data" / DB_FILE_NAME

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
