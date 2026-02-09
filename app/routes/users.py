from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
from pymongo.errors import DuplicateKeyError

from models.user import User

router = APIRouter()


class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str 


@router.post("/", response_model=User)
async def create_user(data: UserCreate):
    try:
        user = User(
            username=data.username,
            email=data.email.lower(),
            password=data.password 
        )
        await user.insert()
        return user
    except DuplicateKeyError:
        raise HTTPException(status_code=400, detail="Email already exists")


@router.get("/", response_model=list[User])
async def list_users():
    return await User.find_all().to_list()


@router.get("/{user_id}", response_model=User)
async def get_user(user_id: str):
    user = await User.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
