from fastapi import APIRouter, HTTPException, Query
from pydantic import BaseModel
from typing import List

from models.message import Message

router = APIRouter()


class MessageCreate(BaseModel):
    room_id: str
    sender_id: str
    content: str


@router.post("/", response_model=Message)
async def send_message(data: MessageCreate):
    message = Message(
        room_id=data.room_id,
        sender_id=data.sender_id,
        content=data.content
    )
    await message.insert()
    return message


@router.get("/room/{room_id}", response_model=List[Message])
async def get_room_messages(
    room_id: str,
    limit: int = Query(50, ge=1, le=100),
    skip: int = 0
):
    return (
        await Message.find(Message.room_id == room_id)
        .sort(-Message.created_at)
        .skip(skip)
        .limit(limit)
        .to_list()
    )
