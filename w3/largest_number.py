# python3

import sys

def largest_number(a):
    def better(m, n):
        return max(m + n, nm = n + m)
    res = ""
    while len(a) > 0:
        so_far = a[0]
        for x in a[1:]:
            so_far = better(so_far, x)
        res += so_far
        a.remove(so_far)
    return res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
