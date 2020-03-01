from random import getrandbits
from DES import Tablici_perestanovok
from PyQt5 import QtWidgets
from DES import des

def mainkey(step):
    key = bin((getrandbits(step)))[2:]
    while len(key) < step:
        key = '0' + key
    return key

def bitichetnosti(key):
    key = list(key)
    for i in range(7, 64, 8):
        key.insert(i, '1')
    return ''.join(key)

def pervonach_perest(key):
    key = list(key)
    num_c, num_d = Tablici_perestanovok.c_d()
    c = [key[i] for i in num_c]
    d = [key[i] for i in num_d]
    return c + d

def obrantaya_perest(mesinbin):
    IP_1 = Tablici_perestanovok.IP_1()
    fin = [mesinbin[i] for i in IP_1]
    return int(''.join(fin), 2)

def sdvig(c, d, num_iter):
    step_shift = Tablici_perestanovok.t_shift()
    sdvig = step_shift[num_iter]
    c = c[sdvig:] + c[:sdvig]
    d = d[sdvig:] + d[:sdvig]
    return c, d

def zaversh_obrab(key):
    matrice = Tablici_perestanovok.rk_last()
    roundkey = [key[i] for i in matrice]
    return ''.join(roundkey)

def generateroundkey(key, num_round):
    c= key[:28]
    d= key[28:]
    c, d = sdvig(c, d, num_round)
    return int(zaversh_obrab(c+d), 2), c+d

def pervonach_perestIP(randbitsmes):
    randbitsmes = list(randbitsmes)
    IP = Tablici_perestanovok.IP()
    mesposleperest = [randbitsmes[i] for i in IP]
    return ''.join(mesposleperest)

def bits2bytes(bits):
    strtoint = int(bits, 2)
    return strtoint.to_bytes(strtoint.bit_length(), 'big')

def str2bits(mes):
    return bin(int.from_bytes(mes.encode(), 'big'))[2:]

def bits2str(c):
    bits=[]
    for i,value in enumerate(spl_str(c,8)):
        bits.append(chr(int(value,2)))
    return ''.join(bits)

def roundkeys(key):
    key = bin(key)[2:]
    while len(key) < 56:
        key = '0' + key
    key = pervonach_perest(bitichetnosti(key) )
    keylst = []
    for num_round in range(1, 17):
        roundkey, key = generateroundkey(key, num_round)
        keylst.append(roundkey)
    return keylst

def block64bits(binmes):
    while (len(binmes) % 64) != 0:
        binmes = '0' + binmes
    bits = spl_str(binmes, 64)
    return bits

def spl_str(str, step):
    bits = []
    str = ''.join(str)
    for i in range (0, len(str), step):
        bits.append(str[i:i+step])
    return bits

def formkeys(n, q, block_size):
    if q == '1':
        key = []
        for i in range(n):
            key.append(getrandbits(block_size // 2))
    else:
        key = [int(i) for i in q.split(' ')]
    return key

def blackbox(tempright, key):
    s = Tablici_perestanovok.s_box()
    tempright = f'{bin(tempright)[2:]:0>48}'
    E = Tablici_perestanovok.E()
    right = [tempright[i] for i in E]
    befs_block = spl_str(f'{bin(int("".join(right),2) ^ key)[2:]:0>48}', 6)
    afts_block = []
    for i in range(len(befs_block)):
        s_bleft = befs_block[i][0] + befs_block[i][-1]
        s_bright =  befs_block[i][1:-1]
        afts_block.append(f'{bin(s[i][s_bleft][s_bright])[2:]:0>4}')
    fin = ''.join(afts_block)
    P = Tablici_perestanovok.P()
    aft_b_box = [fin[i] for i in P]
    f = int(''.join(aft_b_box), 2)
    return f

def cipher(l, r, f):
    left = r
    right = l ^ f
    return left, right

def feistel(mesinbin, n, key):
    left = int(mesinbin[0 : len(mesinbin) // 2], 2)
    right = int(mesinbin[len(mesinbin) // 2:], 2)
    for i in range(n):
        f = blackbox(right, key[i])
        left, right = cipher(left, right, f)
    left = bin(left)[2:]
    right = bin(right)[2:]
    while len(right) < 32:
        right = '0' + right
    while len(left) < 32:
        left = '0' + left
    processed_text = right + left
    return processed_text

def encode(mode, initialialize_vector, mesbits, n, key):
    encbits = ''

    #mesinbytes = message.encode()
    #mesinint = int.from_bytes(mesinbytes, 'big')
    mesblocks = block64bits(mesbits)
    '''
    for block in mesblocks:
        block = pervonach_perestIP(block)
        for i in block64bits(block):
            encbits = encbits + feistel(i, n, keylst)
    '''
    #ECB
    if mode == 1:
        keylst = roundkeys(key[0])
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                encbits += feistel(i, n, keylst)

    #CBC
    elif mode == 2:
        keylst = roundkeys(key[0])
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                i = f'{bin(int(i, 2) ^ initialialize_vector)[2:]:0>64}'
                #print(f'block i after xor: {i}\n')
                encblock = feistel(i, n, keylst)
                encbits += encblock
                initialialize_vector = int(encblock, 2)

    #CFB
    elif mode == 3:
        keylst = roundkeys(key[0])
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                encblock = f'{bin(int(i, 2) ^ int(feistel(initialialize_vector, n, keylst), 2))[2:]:0>64}'
                encbits += encblock
                initialialize_vector = encblock

    #OFВ
    elif mode == 4:
        keylst = roundkeys(key[0])
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                temp = feistel(initialialize_vector, n, keylst)
                encblock = f'{bin(int(i, 2) ^ int(temp, 2))[2:]:0>64}'
                encbits += encblock
                initialialize_vector = temp

    #PCBC
    elif mode == 5:
        keylst = roundkeys(key[0])
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                afx = f'{bin(int(i, 2) ^ initialialize_vector)[2:]:0>64}'
                encblock = feistel(afx, n, keylst)
                encbits += encblock
                initialialize_vector = int(i, 2) ^ int(encblock, 2)

    #BC
    elif mode == 6:
        keylst = roundkeys(key[0])
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                afx = f'{bin(int(i, 2) ^ initialialize_vector)[2:]:0>64}'
                encblock = feistel(afx, n, keylst)
                encbits += encblock
                initialialize_vector = int(encblock, 2)

    #OFBNLF
    elif mode == 7:
        keylst = roundkeys(key[0])
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                temp_key = int(feistel(initialialize_vector, n, keylst), 2)
                round_keylst = roundkeys(temp_key)
                encbits += feistel(i, n, round_keylst)
                initialialize_vector = bin(temp_key)[2:]

    #Простое двойное шифрование
    elif mode == 8:
        round_keylst = []
        keylst = roundkeys(key[0])
        round_keylst.append(keylst)
        keylst2 = roundkeys(key[1])
        round_keylst.append(keylst2)
        for k in round_keylst:
            encbits = ''
            for block in mesblocks:
                temp_block = pervonach_perestIP(block)
                for i in block64bits(temp_block):
                    encbits += feistel(i, n, k)
            mesblocks = block64bits(encbits)

    #Метод Девиса-Прайса
    elif mode == 9:
        keylst = roundkeys(key[0])
        keylst2 = roundkeys(key[1])
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for block in mesblocks:
            for i in block64bits(block):
                asd = feistel(f'{pervonach_perestIP(initialialize_vector):0>64}', n, keylst)
                encblock = f'{bin(int(asd, 2) ^ int(i, 2))[2:]:0>64}'
                initialialize_vector = feistel(f'{pervonach_perestIP(encblock):0>64}', n, keylst2)
                encbits += initialialize_vector

    #Схема тройного шифрования Тачмена (режим EDE)
    elif mode == 10:
        keylst = roundkeys(key[0])
        keylst2 = roundkeys(key[1])
        encbits_last, decbits = '', ''
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                encbits += feistel(i, n, keylst)
        for j in block64bits(encbits):
            decblock = f'{bin(obrantaya_perest(feistel(j, n, keylst2)))[2:]:0>64}'
            decbits += decblock
        for block in block64bits(decbits):
            temp_block_lst = pervonach_perestIP(block)
            for k in block64bits(temp_block_lst):
                encbits_last += feistel(k, n, keylst)
        encbits = encbits_last

    #Тройной алгоритм шифрования с тремя ключами
    elif mode == 11:
        keylst = roundkeys(key[0])
        keylst2 = roundkeys(key[1])
        keylst3 = roundkeys(key[2])
        encbits_last, decbits = '', ''
        for block in mesblocks:
            temp_block = pervonach_perestIP(block)
            for i in block64bits(temp_block):
                encbits += feistel(i, n, keylst)
        for j in block64bits(encbits):
            decblock = f'{bin(obrantaya_perest(feistel(j, n, keylst2)))[2:]:0>64}'
            decbits += decblock
        for block in block64bits(decbits):
            temp_block_lst = pervonach_perestIP(block)
            for k in block64bits(temp_block_lst):
                encbits_last += feistel(k, n, keylst3)
        encbits = encbits_last

    encmesinint = int(encbits, 2)
    encmesinbytes = encmesinint.to_bytes(len(encbits) // 8, 'big')
    #print(encmesinbytes)
    #print(int.from_bytes(encmesinbytes, 'big'))

    #print(f'mesinbytes :\n{int(encbits, 2)}\n\n{int.from_bytes(encmesinbytes, byteorder="big")}')

    try:
        encmes = encmesinbytes.decode('utf-8')
    except Exception:
        encmes = encmesinint
    #encmes = bits2str(encbits)

    return encmes, encbits

def decode(mode, initialialize_vector, encbits, n, key):
    decbits, plain , temp = '', '', ''

    '''
    for i in block64bits(encbits):
        decbits = feistel(i, n, keylst)
        temp = bin(obrantaya_perest(decbits))[2:]
        while len(temp) < 64:
            temp = '0' + temp
        plain += temp
    mesinbits = plain
    '''
    #ECB
    if mode == 1:
        keylst = roundkeys(key[0])
        keylst.reverse()
        for i in block64bits(encbits):
            decblock = f'{bin(obrantaya_perest(feistel(i, n, keylst)))[2:]:0>64}'
            decbits += decblock

    #CBC
    elif mode == 2:
        keylst = roundkeys(key[0])
        keylst.reverse()
        temp = []
        for i in block64bits(encbits):
            decblock = feistel(i, n, keylst)
            decbits = f'{bin(int(decblock, 2) ^ initialialize_vector)[2:]:0>64}'
            initialialize_vector = int(i, 2)
            temp.append(decbits)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #CFB
    elif mode == 3:
        keylst = roundkeys(key[0])
        temp = []
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for i in block64bits(encbits):
            decblock = feistel(initialialize_vector, n, keylst)
            decbits = f'{bin(int(decblock, 2) ^ int(i, 2))[2:]:0>64}'
            initialialize_vector = i
            temp.append(decbits)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #OFВ
    elif mode == 4:
        keylst = roundkeys(key[0])
        temp = []
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for i in block64bits(encbits):
            decblock = feistel(initialialize_vector, n, keylst)
            decbits = f'{bin(int(decblock, 2) ^ int(i, 2))[2:]:0>64}'
            initialialize_vector = decblock
            temp.append(decbits)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #PCBC
    elif mode == 5:
        keylst = roundkeys(key[0])
        keylst.reverse()
        temp = []
        for i in block64bits(encbits):
            decblock = int(feistel(i, n, keylst), 2) ^ initialialize_vector
            decbits = f'{bin(decblock)[2:]:0>64}'
            initialialize_vector = int(i, 2) ^ decblock
            temp.append(decbits)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #BC
    elif mode == 6:
        keylst = roundkeys(key[0])
        keylst.reverse()
        temp = []
        for i in block64bits(encbits):
            decblock = int(feistel(i, n, keylst), 2) ^ initialialize_vector
            decbits = f'{bin(decblock)[2:]:0>64}'
            initialialize_vector = int(i, 2)
            temp.append(decbits)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #OFBNLF
    elif mode == 7:
        temp = []
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        temp_k = roundkeys(key[0])
        for i in block64bits(encbits):
            temp_key = int(feistel(initialialize_vector, n, temp_k), 2)
            round_keylst = roundkeys(temp_key)
            round_keylst.reverse()
            decblock = feistel(i, n, round_keylst)
            initialialize_vector = bin(temp_key)[2:]
            temp.append(decblock)
        decbits = ''
        for i in temp:
            res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
            decbits += res

    #Простое двойное шифрование
    elif mode == 8:
        temp, round_keylst = [], []
        round_keylst = []
        keylst = roundkeys(key[0])
        keylst.reverse()
        round_keylst.append(keylst)
        keylst2 = roundkeys(key[1])
        keylst2.reverse()
        round_keylst.append(keylst2)
        round_keylst.reverse()
        mesblocks = block64bits(encbits)
        for k in round_keylst:
            encbits = ''
            for i in mesblocks:
                decbits = feistel(i, n, k)
                temp.append(decbits)
            decbits = ''
            for i in temp:
                res = f'{bin(obrantaya_perest(i))[2:]:0>64}'
                decbits += res
            temp = []
            mesblocks = block64bits(decbits)

    #Метод Девиса-Прайса
    elif mode == 9:
        keylst = roundkeys(key[0])
        keylst2 = roundkeys(key[1])
        keylst2.reverse()
        temp = []
        decbits = ''
        initialialize_vector = f'{bin(initialialize_vector)[2:]:0>64}'
        for i in block64bits(encbits):
            encblock = feistel(pervonach_perestIP(initialialize_vector), n, keylst)
            decblock = f'{bin(obrantaya_perest(feistel(i, n, keylst2)))[2:]:0>64}'
            decbits += f'{bin(int(decblock, 2) ^ int(encblock, 2))[2:]:0>64}'
            initialialize_vector = i

    #Схема тройного шифрования Тачмена (режим EDE)
    elif mode == 10:
        keylst = roundkeys(key[0])
        keylst.reverse()
        keylst2 = roundkeys(key[1])
        keylst2.reverse()
        decbits = ''
        for i in block64bits(encbits):
            decblock = f'{bin(obrantaya_perest(feistel(i, n, keylst)))[2:]:0>64}'
            encblock = feistel(pervonach_perestIP(decblock), n, keylst2)
            decblock = f'{bin(obrantaya_perest(feistel(encblock, n, keylst)))[2:]:0>64}'
            decbits += decblock

    #Тройной алгоритм шифрования с тремя ключами
    elif mode == 11:
        keylst = roundkeys(key[0])
        keylst.reverse()
        keylst2 = roundkeys(key[1])
        keylst2.reverse()
        keylst3 = roundkeys(key[2])
        keylst3.reverse()
        decbits = ''
        for i in block64bits(encbits):
            decblock = f'{bin(obrantaya_perest(feistel(i, n, keylst3)))[2:]:0>64}'
            encblock = feistel(pervonach_perestIP(decblock), n, keylst2)
            decblock = f'{bin(obrantaya_perest(feistel(encblock, n, keylst)))[2:]:0>64}'
            decbits += decblock

    dec = int(decbits, 2)
    try:
        decmes = dec.to_bytes(dec.bit_length(), 'big').decode().replace('\x00','')
    except Exception:
        #print("Can't decode bytes")
        decmes = dec
    return decmes, decbits

def main():
    initialialize_vector = getrandbits(56)
    some_txt = 'asdqwe 123123 1232'
    mesinbytes = some_txt.encode()
    mesinint = int.from_bytes(mesinbytes, 'big')
    message = bin(mesinint)[2:]
    #print(f'mes in bin {message}')
    encmes, encbits = encode(9, initialialize_vector, message, 16, [1375218624468556, 5050552611588013, 20602454714711512])
    decmes, decbits = decode(9, initialialize_vector, encbits, 16, [1375218624468556, 5050552611588013, 20602454714711512])
    print(some_txt)
    #print(f'dec in bin {decbits}')
    print(decmes)


if __name__ == '__main__':
    main()
