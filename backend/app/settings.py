from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DOTENV_PATH = BASE_DIR / ".env"


class CoreSettings(BaseSettings):
    APP_NAME: str = "HoroShop"
    DEBUG: bool = True


class PostgresSettings(BaseSettings):
    PGHOST: str
    PGDATABASE: str
    PGUSER: str
    PGPASSWORD: str
    PGPORT: int = 5432

    # Додаємо конфігурацію саме сюди або в спільний клас Settings
    model_config = SettingsConfigDict(
        env_file=DOTENV_PATH,
        env_file_encoding="utf-8",
        extra="ignore"
    )

    @property
    def DATABASE_ASYNC_URL(self) -> str:
        return (
            f"postgresql+asyncpg://{self.PGUSER}:{self.PGPASSWORD}@"
            f"{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}"
        )


class Settings(CoreSettings, PostgresSettings):
    pass


@lru_cache(maxsize=None)
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
