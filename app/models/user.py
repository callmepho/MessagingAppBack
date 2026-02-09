from pydantic import EmailStr, Field
from typing import Optional, Literal
from datetime import datetime
from beanie import Document
from pymongo import IndexModel

class User(Document):
    username: str
    email: EmailStr
    password: str

    avatar_url: Optional[str] = None
    status: Literal["online", "offline", "away"] = "offline"
    last_seen: Optional[datetime] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "users"
        indexes = [
            IndexModel([("email", 1)], unique=True),
        ]
