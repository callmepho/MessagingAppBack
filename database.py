from motor.motor_asyncio import AsyncIOMotorClient 
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv
import os
from beanie import init_beanie


from models.user import User
from models.room import Room
from models.message import Message

load_dotenv()

MONGO_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")

client: AsyncIOMotorClient | None = None

async def connect_mongo():
    global client

    try:
        client = AsyncIOMotorClient (
            MONGO_URI,
            serverSelectionTimeoutMS=5000
        )

        await client.admin.command("ping")

        await init_beanie(
        database=client[DB_NAME],
        document_models=[
            User,
            Room,
            Message,
        ],
    )
        print("MongoDB connected")

    except ServerSelectionTimeoutError as e:
        print("MongoDB connection failed")
        raise e
    
async def disconnect_mongo():
    global client
    if client:
        client.close()
        print("MongoDB disconnected")