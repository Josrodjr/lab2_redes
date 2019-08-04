import socket
import en_decript as ed
import noise as noise
import crc as crc
import ham as ham

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
message = 'Connected\n'
client.send(message.encode())
from_server = client.recv(4096)

a = ed.str_to_BIN('holaquetal')
b = ed.bitarray_to_BIN(from_server)

crcSays = crc.crc(b)
hamming = ham.hamming(b)
hammingB = ham.hamming_to_BIT(hamming)
print("CRC: " + crcSays)
print(ham.compare_efficency(a, hammingB))

client.send(crcSays.encode())

client.close()