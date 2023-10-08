from pydantic_settings import BaseSettings, SettingsConfigDict


class TestUser(BaseSettings):
    email: str = ""
    password: str = ""


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8',
        env_nested_delimiter='.'
    )

    base_url: str
    test_user: TestUser = TestUser()

    @property
    def api_url(self) -> str:
        return f'{self.base_url}/futurama'


base_settings = Settings()
