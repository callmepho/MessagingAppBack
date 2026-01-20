from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime
from beanie import Document


class RoomMember(BaseModel):
  user_id: str
  joined_at: datetime = datetime.now()


class LastMessagePreview(BaseModel):
  message_id: str
  sender_id: str
  content_preview: str
  created_at: datetime


class Room(Document):
  members: List[RoomMember]

  name: Optional[str] = None

  last_message: Optional[LastMessagePreview] = None

  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()
  
  class Settings:
    name = "rooms"