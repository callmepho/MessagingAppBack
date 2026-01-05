from pydantic import BaseModel
from typing import List, Optional, Literal
from datetime import datetime


class RoomMember(BaseModel):
  user_id: str
  joined_at: datetime = datetime.now()


class LastMessagePreview(BaseModel):
  message_id: str
  sender_id: str
  content_preview: str
  created_at: datetime


class Room(BaseModel):
  id: Optional[str] = None

  type: Literal["direct", "group"]
  members: List[RoomMember]

  name: Optional[str] = None

  last_message: Optional[LastMessagePreview] = None

  created_at: datetime = datetime.now()
  updated_at: datetime = datetime.now()