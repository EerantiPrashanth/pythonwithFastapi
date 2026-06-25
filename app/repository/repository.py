from bson import ObjectId
from app.db.mongo import users_collection

async def create_user_repo(data: dict):
    result = await users_collection.insert_one(data)
    return str(result.inserted_id)


async def get_users_repo():
    return await users_collection.find().to_list(100)


async def get_user_repo(user_id: str):
    return await users_collection.find_one({"_id": ObjectId(user_id)})


async def update_user_repo(user_id: str, data: dict):
    await users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$set": data}
    )


async def delete_user_repo(user_id: str):
    await users_collection.delete_one({"_id": ObjectId(user_id)})