from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio
from socket import sio
from database import connect_mongo,disconnect_mongo


app = FastAPI(
    title="Realtime Messaging API",
    version="1.0.0"
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

