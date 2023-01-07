from pydantic import BaseModel, BaseSettings, Field


class TestUser(BaseModel):
    email: str
    password: str


class Settings(BaseSettings):
    base_url: str = Field(..., env='BASE_URL')
    user_email: str = Field(..., env='TEST_USER_EMAIL')
    user_password: str = Field(..., env='TEST_USER_PASSWORD')

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'

    @property
    def api_url(self) -> str:
        return f'{self.base_url}/futurama'

    @property
    def user(self) -> TestUser:
        return TestUser(
            email=self.user_email,
            password=self.user_password
        )


base_settings = Settings()
