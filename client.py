import socket
import en_decript as ed
import noise as noise
import crc as crc
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('0.0.0.0', 8080))
message = 'Connected\n'
client.send(message.encode())
from_server = client.recv(4096)

b = ed.bitarray_to_BIN(from_server)

ans = crc.crc(b, "1001") 
print("Remainder after decoding is->"+ans) 
    
# If remainder is all zeros then no error occured 
temp = "0" * (len("1001") - 1) 
noerror = 'No error FOUND'
error = 'Error in data'
if ans == temp: 
    client.send(noerror.encode()) 
else: 
    client.send(error.encode()) 
client.close()