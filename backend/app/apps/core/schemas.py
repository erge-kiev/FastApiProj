from pydantic import BaseModel, Field
from pygments.lexers import special


class IdSchema(BaseModel):
    id: int = Field(examples=[1234], gt=0)
