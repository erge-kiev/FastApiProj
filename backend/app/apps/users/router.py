from fastapi import APIRouter, status

from apps.users.schemas import RegisterUserSchema, RegisteredUserSchema

router_users = APIRouter()


@router_users.post("/create", status_code=status.HTTP_201_CREATED)
async def create_user(new_user: RegisterUserSchema) -> RegisteredUserSchema:
    created_user = RegisteredUserSchema(id=287681726, **new_user.dict())
    return created_user
