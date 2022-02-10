from pathlib import Path

from pydantic import BaseSettings


DEFAULT_LOGGING_SETTING_FILENAME = "logging-console.yaml"


class Settings(BaseSettings):
    LOGGING_CONF_PATH: str = str(Path(__file__).parents[1] / DEFAULT_LOGGING_SETTING_FILENAME)


settings = Settings()
