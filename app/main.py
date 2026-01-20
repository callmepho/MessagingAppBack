from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from socketio_server import sio
from database import connect_mongo,disconnect_mongo


@asynccontextmanager
async def lifespan(app: FastAPI):
    await connect_mongo()
    yield
    await disconnect_mongo()


app = FastAPI(
    title="Realtime Messaging API",
    version="1.0.0",
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",  
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


socket_app = socketio.ASGIApp(sio, app)

