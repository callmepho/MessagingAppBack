from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Literal, Optional

from models.room import Room

router = APIRouter()


class RoomCreate(BaseModel):
    member_ids: List[str]
    name: Optional[str] = None


@router.post("/", response_model=Room)
async def create_room(data: RoomCreate):
    room = Room(
        type=data.type,
        member_ids=data.member_ids,
        name=data.name
    )
    await room.insert()
    return room


@router.get("/", response_model=list[Room])
async def list_rooms():
    return await Room.find_all().to_list()


@router.get("/{room_id}", response_model=Room)
async def get_room(room_id: str):
    room = await Room.get(room_id)
    if not room:
        raise HTTPException(status_code=404, detail="Room not found")
    return room
