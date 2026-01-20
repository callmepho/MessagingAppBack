from pydantic import EmailStr
from typing import Optional, Literal
from datetime import datetime
from beanie import Document

class User(Document):
  id: Optional[str] = None

  username: str
  email: EmailStr
  password_hash: str

  avatar_url: Optional[str] = None

  status: Literal["online", "offline", "away"] = "offline"
  last_seen: Optional[datetime] = None

  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()

  class Settings:
    name = "users"
    indexes = [
      {
        "key": "email",
        "unique": True
      }
    ]