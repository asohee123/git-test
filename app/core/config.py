from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    APP_NAME: str = "git-test-app"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = False

    class Config:
        env_file = ".env"


settings = Settings()
