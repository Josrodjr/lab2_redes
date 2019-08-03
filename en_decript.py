import bitarray


def str_to_BIN(string):
    a = bin(int.from_bytes(string.encode(), 'big'))[2:]
    # remove the first two ('0b') esta arriba 
    return a


def BIN_to_str(bits, encoding='utf-8', errors='surrogatepass'):
    b = int(bits, 2)
    return b.to_bytes((b.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'



def BIN_to_bitarray(bin):
    a = bitarray.bitarray(bin)
    return a


def bitarray_to_BIN(barray):
    # a = barray.to_bytes()
    # a = bytes(barray)
    # a = barray.decode('utf-8')
    a = bin ( int.from_bytes(barray, 'big', signed=False) )[2:]
    b = a[:-1]
    return b

# zero = str_to_BIN('pepapls')
# print(zero)

# a = BIN_to_bitarray(zero)
# print(a)

# b = bitarray_to_BIN(a)
# print(b)

# c = BIN_to_str(b)
# print(c)