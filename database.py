from pymongo import AsyncMongoClient
from pymongo.errors import ServerSelectionTimeoutError
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URI = os.getenv("DB_URI")
DB_NAME = os.getenv("MONGO_DB_NAME")

client: AsyncMongoClient | None = None
db = None

async def connect_mongo():
    global client, db

    try:
        client = AsyncMongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000
        )

        await client.admin.command("ping")

        db = client[DB_NAME]
        print("MongoDB connected")

    except ServerSelectionTimeoutError as e:
        print("MongoDB connection failed")
        raise e
    
async def disconnect_mongo():
    global client
    if client:
        await client.close()
        print("MongoDB disconnected")