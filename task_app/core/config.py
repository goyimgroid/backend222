from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy.engine import URL


class Settings(BaseSettings):
    db_host: str
    db_port: int
    db_user: str
    db_password: str
    db_name: str

    # extra="ignore" - чтобы лишние переменные в .env не ломали запуск
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()

# URL.create сам экранирует спецсимволы в пароле (@, :, / и т.д.)
DB_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=settings.db_port,
    database=settings.db_name,
)