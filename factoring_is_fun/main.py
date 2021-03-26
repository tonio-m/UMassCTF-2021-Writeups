# dar o ncat nisso 34.69.184.228:8080
import time
import math
import random
from pwn import * 

def getMask(p):
        r = random.seed(0)
        global block
        block = None
        if block == None:
            bit_count = math.floor(64 *((time.time() - start_time) / (end_time - start_time))) 
        else:
            bit_count = block
        m = []
        for i in range(64):
            m.append(i)
        bit_mask = [0] * 64

        for i in range(bit_count):
            curr = random.randint(0,len(m))
            bit_mask[m[curr]] = 1
            m.remove(m[curr])

        p = bin(p)[2:]
        ret = ''
        for i, c in enumerate(p):
            if bit_mask[i // 8] == 0:
                ret += '?'
            else:
                ret += p[i]
        return ret


if __name__ == '__main__':
    r = remote('34.69.184.228', 8080)
    r.interactive()
