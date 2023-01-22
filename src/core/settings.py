from pydantic import BaseSettings


class APISettings(BaseSettings):

    HOST: str
    PORT: int
    LOG_LEVEL: str = "INFO"
    RELOAD: bool = False

    class Config:
        case_sensitive = True
        env_file = ".env"
        env_file_encoding = "utf-8"
        env_prefix = "API_"


api_settings = APISettings()
