from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
DB_NAME = os.getenv("DB_NAME")

print("MONGO_URI:-",MONGODB_URI)
print("DB_NAME:-",DB_NAME)

client = AsyncIOMotorClient(MONGODB_URI)
db = client[DB_NAME]

users_collection = db["users"]
