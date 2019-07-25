import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')

app = web.Application()
sio.attach(app)


# app = socketio.WSGIApp(socket_io)

# @socket_io.event
# def connect(sid, data):
#     print("A connection")
#     pass

@sio.event
async def connect(sid, environ):
    await sio.emit('yeet', {'data': 'yeeted'})
    print('connect ', sid)

@sio.event
async def disconnect(sid):
    print('disconnect ', sid)


if __name__ == '__main__':
    web.run_app(app)