#!/usr/bin/env python3

def encrypt(data, key):
    res = []
    for i in range(len(data)):
        res.append(data[i] ^ key[i % 4])
    return bytes(res)


print('Enter a key: ')
key = input()
key = key.encode('ascii')[:4]

data = open('data.gif', 'rb').read()

encrypted = encrypt(data, key)

fout = open('data.gif.encrypted', 'wb')
fout.write(encrypted)
fout.close()
