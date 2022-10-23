from typing import Optional

from pydantic import BaseSettings, PostgresDsn


class _Settings(BaseSettings):
    log_level: str = "INFO"

    class Config:
        env_file = ".env"


class _UvicornSettings(BaseSettings):
    workers: Optional[int] = None
    port = 8000
    host = "localhost"

    class Config:
        env_file = ".env"
        env_prefix = "uvicorn_"


class _AppSettings(BaseSettings):
    local_run: bool = False
    show_swagger: bool = False
    allowed_origins_regex: str = "^.+$"

    class Config:
        env_file = ".env"
        env_prefix = "app_"


class _DBSettings(BaseSettings):
    dsn: Optional[PostgresDsn] = None
    autocommit: bool = False

    class Config:
        env_file = ".env"
        env_prefix = "db_"


class _SecuritySettings(BaseSettings):
    yc_token: Optional[str] = None
    yc_access_key: Optional[str] = None
    yc_secret_key: Optional[str] = None

    class Config:
        env_file = ".env"
        env_prefix = "security_"


class _PredictionService(BaseSettings):
    base_host_url: str = "http://178.154.222.99:8000"

    class Config:
        env_file = ".env"
        env_prefix = "predict_"


class _S3Settings(BaseSettings):
    endpoint: str = "https://storage.yandexcloud.net"
    bucket_name: str = "ml-files"


s3_settings = _S3Settings()
db_settings = _DBSettings()
settings = _Settings()
app_settings = _AppSettings()
security_settings = _SecuritySettings()
uvicorn_settings = _UvicornSettings()
prediction_service = _PredictionService()
