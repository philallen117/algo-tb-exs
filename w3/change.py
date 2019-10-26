# python3
import sys

def get_change(m):
    #write your code here
    assert(m >= 1)
    denoms = [10, 5, 1]
    coins = 0
    for d in denoms:
        num_d = m // d
        coins = coins + num_d
        m = m % d
    return coins

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
