# python3

import sys
from math import floor, log10, pow

def largest_number(a):
    # def most_sig_dig(i):
    #     return floor(i / pow(10, floor(log10(i))))
    def most_sig_dig(i):
        r = i
        while r >= 10:
            r = i // 10
        return r
    a_msd = [most_sig_dig(i) for i in a]
    res = ""
    for x in a:
        res += x
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
