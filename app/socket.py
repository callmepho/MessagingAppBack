import socketio

sio = socketio.AsyncServer(
    async_mode="asgi",
    cors_allowed_origins="*"
)

@sio.event
async def connect(sid, environ):
    print(f"🔌 Client connected: {sid}")

@sio.event
async def disconnect(sid):
    print(f"❌ Client disconnected: {sid}")

@sio.event
async def join_room(sid, room_id):
    await sio.enter_room(sid, room_id)
    print(f"➡️ {sid} joined room {room_id}")

@sio.event
async def send_message(sid, data):
    await sio.emit(
        "new_message",
        data,
        room=data["roomId"]
    )