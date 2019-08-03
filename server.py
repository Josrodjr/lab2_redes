import socket
import en_decript as ed
import noise as noise
import ham as ham

serv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv.bind(('0.0.0.0', 8080))
serv.listen(5)

while True:
    conn, addr = serv.accept()
    from_client = ''
    while True:
        data = conn.recv(4096)
        if not data: break
        from_client += data.decode()
        a = ed.str_to_BIN('pepapls')
        b = noise.add_noise(a, 0.1)
        message = ed.BIN_to_bitarray(b)
        conn.send(message)
    conn.close()
    print ('client disconnected')