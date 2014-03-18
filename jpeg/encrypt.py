#!/usr/bin/env python3

KEY_LEN = 16


def encrypt(data, key):
    assert isinstance(data, bytes)

    summand = 7

    output = []
    for i, char in enumerate(data):
        tmp = (char + key[i % KEY_LEN] + summand) % 256
        output.append(tmp)
        summand ^= (39 * tmp + 23) % 256

    return bytes(output)


key = input('Enter {0}-character key: '.format(KEY_LEN))
key = key.encode('ascii')
if len(key) != KEY_LEN:
    print('Invalid key length')
    sys.exit(1)

data = open('source.jpg', 'rb').read()

with open('dest.jpg', 'wb') as fout:
    fout.write(encrypt(data, key))
