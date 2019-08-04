
def bitpar(bits):
    i = 0
    while 2**i <= bits+i:
        i = i + 1
    return i 


def bitpar_corr(bits):
    i = 0
    while 2**i <= bits:
        i = i + 1
    return i 

def app_bitpar(bits):
    n = bitpar(len(bits))
    i = 0
    j = 0
    k = 0
    list_ = list()
    while i < n + len(bits):
        if i == (2 ** j - 1):
            list_.insert(i, 0)
            j = j + 1
        else:
            list_.insert(i, bits[k])
            k = k + 1
        i = i + 1
    return list_

def hamming(bits):
    n = bitpar_corr(len(bits))
    lst = app_bitpar(bits)
    i = 0
    k = 1 
    errorthBit=0
    while k < n:
        k = 2 ** i
        j = 1
        total = 0
        while j * k - 1 < len(lst):
            if j*k - 1 == len(lst) - 1:
                l_index = j * k -1
                t = lst[int(l_index):len(lst)]
            elif (j + 1)*k - 1 >= len(lst):
                l_index = j * k - 1
                t = lst[int(l_index):len(lst)]
            elif (j + 1)*k -1 < len(lst) - 1:
                l_index = (j * k) - 1
                u_index = (j + 1)*k - 1
                t = lst[int(l_index): int(u_index)]
            
            total = total + sum(int(e) for e in t)
            #print(t, j)
            j = j + 2
        if total%2 > 0:
            lst[int(k) - 1] = 1
            #print("El elemento es: " + str(lst[int(k)-1]) + " " + str(k))
        i = i + 1
    if errorthBit>=1:
        #print ("Hamming: error in " + str(errorthBit) + " bit after correction data is " )
        if lst[int(errorthBit - 1)] =='0' or lst[int(errorthBit - 1)] == 0:
            lst[int(errorthBit - 1)] = '1'
        else:
            lst[int(errorthBit - 1)] = '0'
    else:
        #print("Hamming: NO ERROR") 
        print(" ")
    i=0
    j=0
    k=0
    list_ = list()
    while i<len(lst):
        if i!= ((2 ** k) - 1):
            temp=lst[int(i)]
            list_.append(temp)
            j = j + 1
        else:
            k+=1
        i+=1
    return list_


def hamming_to_BIT(haming):
    total = ''
    for value in haming:
        total = total + value
    return total

def compare_efficency(original, noise_corrected):
    good = 0
    wrong = 0
    if len(original) == len(noise_corrected):
        for i in range(len(original)):
            if original[i] == noise_corrected[i]:
                good = good + 1
            else:
                wrong = wrong + 1 
    total = good + wrong
    efficiency = (good / total) * 100
    return efficiency

# hacer hamming sobre un string con noise
#a = hamming('0110000001011010111000101100001011100000110110001111111')

# convertir a un arreglo de bits
#b = hamming_to_BIT(a)

# comparar que tan efectivo fue hamming
#print(compare_efficency('1110000011001010111000001100001011100000110110001110011', b))