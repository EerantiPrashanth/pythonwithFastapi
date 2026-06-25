from app.repository.repository import (
    create_user_repo,
    get_users_repo,
    get_user_repo,
    update_user_repo,
    delete_user_repo
)


def serialize_user(user):
    if not user:
        return None
    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "age" : user["age"],
        "phone":user["phone"],
        "address" : user["address"]
    }


async def create_user_service(data: dict):
    return await create_user_repo(data)


async def get_users_service():
    users = await get_users_repo()
    return [serialize_user(u) for u in users]


async def get_user_service(user_id: str):
    user = await get_user_repo(user_id)
    return serialize_user(user)


async def update_user_service(user_id: str, data: dict):
    return await update_user_repo(user_id, data)


async def delete_user_service(user_id: str):
    return await delete_user_repo(user_id)