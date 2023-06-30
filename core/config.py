from pydantic import BaseSettings, Field


class Settings(BaseSettings):
    TG_BOT_API_KEY: str
    TG_USER_ID: int
    SERVICE_URL: str = Field("https://coinranking.com")
    TASKS_JSON_PATH: str = Field("./data/tasks.json")
    COINS_JSON_PATH: str = Field("./data/coins.json")

    class Config:
        case_sensitive = True
        env_file = "config.env"


project_settings = Settings()
