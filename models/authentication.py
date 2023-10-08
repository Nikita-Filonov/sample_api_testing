from pydantic import BaseModel, Field, model_validator

from settings import base_settings


class AuthUser(BaseModel):
    email: str = Field(default=base_settings.test_user.email)
    password: str = Field(default=base_settings.test_user.password)


class Authentication(BaseModel):
    auth_token: str | None = None
    user: AuthUser | None = AuthUser()

    @model_validator(mode='after')
    def validate_root(self) -> 'Authentication':
        if (not self.auth_token) and (not self.user):
            raise ValueError(
                'Please provide "username" and "password" or "auth_token"'
            )

        return self
