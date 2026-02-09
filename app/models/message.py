from typing import Optional, Literal, List
from datetime import datetime
from beanie import Document

class Message(Document):
  room_id: str
  sender_id: str

  type: Literal["text", "image"] = "text"
  content: str

  metadata: Optional[dict] = None

  read_by: List[str] = []

  created_at: datetime = datetime.now()
  edited_at: Optional[datetime] = None
  deleted_at: Optional[datetime] = None

  class Settings:
    name = "messages"
    indexes = [
        [("room_id", 1), ("created_at", -1)]
    ]