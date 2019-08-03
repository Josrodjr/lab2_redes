import socket
import en_decript as ed
import noise as noise
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
message = 'Connected'
client.send(message.encode())
from_server = client.recv(4096)
client.close()
b = ed.bitarray_to_BIN(from_server)
c = ed.BIN_to_str(b)
print (c)