from typing import Any

from pydantic import Field, ValidationError, root_validator

from settings import base_settings
from utils.models.base_model import BaseModel


class AuthUser(BaseModel):
    email: str = Field(default=base_settings.user.email)
    password: str = Field(default=base_settings.user.password)


class Authentication(BaseModel):
    auth_token: str | None
    user: AuthUser | None = AuthUser()

    @root_validator
    def validate_root(cls, values: dict[str, Any]) -> dict[str, Any]:
        if (not values["auth_token"]) and (not values["user"]):
            raise ValidationError(
                'Please provide "username" and "password" or "auth_token"'
            )

        return values
