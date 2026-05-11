import numbers
from typing import Annotated
from pydantic import BaseModel, EmailStr, Field, StringConstraints, field_validator
from password_strength import PasswordPolicy
from pygments.lexers import special

from apps.core.schemas import IdSchema


class UserPasswordSchema(BaseModel):
    password: str = Field(examples=["lkjlKJJ1#kkml"])

    @field_validator("password")
    @classmethod
    def validate_password_complexity(cls, value: str) -> str:
        password_policy = PasswordPolicy.from_names(
            length=8,
            uppercase=True,
            numbers=1,
            special=1
        )

        errors = password_policy.test(value)
        if not errors:
            return value

        error_messages = []
        for error in errors:
            error_name = error.name()
            if error_name == "length":
                error_messages.append(f"Password must be at least 8 characters long.")
            elif error_name == "uppercase":
                error_messages.append(f"Password must be at Upper Case letters.")

        raise ValueError("; ".join(error_messages))


class BaseUserSchema(BaseModel):
    email: EmailStr = Field(description="Email address", examples=["email.ukr.net"])
    name: Annotated[
        str, StringConstraints(pattern=r"^[a-zA-Z0-9_-]+$", strip_whitespace=True, min_length=3, max_length=50)]


class RegisterUserSchema(BaseUserSchema, UserPasswordSchema):
    pass


class RegisteredUserSchema(IdSchema, BaseUserSchema):
    pass
