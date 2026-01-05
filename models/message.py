from typing import Optional, Literal, List
from pydantic import BaseModel
from datetime import datetime

class Message(BaseModel):
  id: Optional[str] = None

  room_id: str
  sender_id: str

  type: Literal["text", "image", "file"] = "text"
  content: str

  metadata: Optional[dict] = None

  read_by: List[str] = []

  created_at: datetime = datetime.now()
  edited_at: Optional[datetime] = None
  deleted_at: Optional[datetime] = None