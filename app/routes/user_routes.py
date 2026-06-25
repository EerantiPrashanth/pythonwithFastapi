from fastapi import APIRouter
from app.schema.user_schema import User , UpdateUser
from app.services.service import (
    create_user_service,
    get_users_service,
    get_user_service,
    update_user_service,
    delete_user_service
)

router = APIRouter()

@router.post("/users")
async def create_user(user: User):
    user_id = await create_user_service(user.dict())
    return {"id": user_id}


@router.get("/users")
async def get_users():
    return await get_users_service()


@router.get("/users/{user_id}")
async def get_user(user_id: str):
    return await get_user_service(user_id)


@router.put("/users/{user_id}")
async def update_user(user_id: str, user: UpdateUser):
    await update_user_service(user_id, user.dict(exclude_none=True)) # here excluded_none ensure that only provided values are updated 
    return {"message": "updated"}


@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    await delete_user_service(user_id)
    return {"message": "deleted"}