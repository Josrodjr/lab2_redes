import socketio
import asyncio

loop = asyncio.get_event_loop()

HOST_PORT = 'http://0.0.0.0:8080'

sio = socketio.AsyncClient()

# sio.connect(HOST_PORT)


@sio.event
async def connect():
    print('I\'m connected!')
    # socket_io.emit('signin', {
    #     'user_name': USER_NAME,
    #     'tournament_id': 5,
    #     'user_role': 'player'
    #     })


async def start_server():
    await sio.connect('http://0.0.0.0:8080')
    await sio.wait()


if __name__ == '__main__':
    loop.run_until_complete(start_server())