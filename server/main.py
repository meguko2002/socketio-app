from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socketio

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
async def home():
    print('get_request')
    return {'message': 'Hello👋 Developers💻'}

# socket_io
sio_server = socketio.AsyncServer(cors_allowed_origins='*', async_mode='asgi')
socketio_app = socketio.ASGIApp(sio_server, app)


@sio_server.event
async def connect(sid, environ, auth):
    print(f'{sid}: connected')
    await sio_server.emit('join', {'sid': sid})


@sio_server.event
async def chat(sid, message):
    print(message)
    await sio_server.emit('chat', {'sid': sid, 'message': message})


@sio_server.event
async def disconnect(sid):
    print(f'{sid}: disconnected')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:socketio_app", host='127.0.0.1', port=8000, reload=True)
