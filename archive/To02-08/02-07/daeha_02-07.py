#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Cryptographic examples

"""        
import sys
import time
from concurrent import futures
from random import randrange
#from arcfour import arcfour


JOBS = 12
SIZE = 2**18

KEY = b"'Twas brilling, and the slithy toves\nDid gyre"  # bytes
STATUS = '{} workers, elapsed time: {:.2f}s'


def arcfour(key, in_bytes, loops=20):
    """RC4 compatible algorithm"""
    
    kbox = bytearray(256)  # create key box
    for i, car in enumerate(key):  # copy key and vector
        kbox[i] = car
    j = len(key)
    for i in range(j, 256):  # repeat until full
        kbox[i] = kbox[i-j]
        
    # [1] initialize sbox
    sbox = bytearray(range(256))
    
    # repeat sbox mixing loop, as recommend in CipherSaber-2
    # http://ciphersaber.gurus.com/faq.html#cs2
    j = 0
    for k in range(loops):
        for i in range(256):
            j = (j + sbox[i] + kbox[i]) % 256
            sbox[i], sbox[i] = sbox[j], sbox[i]
            
    # main loop
    i = 0; j = 0
    out_bytes = bytearray()
    
    for car in in_bytes:
        i = (i + 1) % 256
        # [2] shuffle sbox
        j = (j + sbox[i]) % 256
        sbox[i], sbox[j] = sbox[j], sbox[i]
        # [3] compute t
        t = (sbox[i] + sbox[j]) % 256
        k = sbox[t]
        car = car ^ k
        out_bytes.append(car)
        
    return out_bytes
    
    
def arcfour_test(size, key):
    in_text = bytearray(randrange(256) for i in range(size))
    cypher_text = arcfour(key, in_text)
    print('cypher_text is: {}'.format(cypher_text))
    out_text = arcfour(key, cypher_text)
    assert in_text == out_text, 'Failed arcfour_test'
    return size


def main(workers=None):
    if workers:
        workers = int(workers)
    t0 = time.time()
    
    with futures.ProcessPoolExecutor(workers) as executor:
        actual_workers = executor._max_workers
        print('actural workers is: {}'.format(actual_workers))  # default is 4 ( In case of my notebook :) )
        to_do = []
        for i in range(JOBS, 0, -1):
            size = SIZE + int(SIZE / JOBS * (i - JOBS/2))
            job = executor.submit(arcfour_test, size, KEY)
            to_do.append(job)
            #print('to_do: {}'.format(to_do))  # <Future at 0x10f23c5f8 state=running>, <Future at 0x10f23c8d0 state=pending>
            
        for future in futures.as_completed(to_do):
            res = future.result()
            print('{:.1f} KB'.format(res/2**10))
            
    print(STATUS.format(actual_workers, time.time() - t0))
    
    
if __name__ == '__main__':
    if len(sys.argv) == 2:
        workers = int(sys.argv[1])
    else:
        workers = None
    main(workers)