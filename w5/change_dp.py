# Uses python3
import sys
import array as a

max_m = 1000
denominations = [1, 3, 4]

def get_change(m):
    least_coins = a.array('I', [0] * (m + 1))
    for i in range(1, m+1):
        best = sys.maxsize
        for d in denominations:
            if d <= i:
                current = 1 + least_coins[i - d]
                best = min(current, best)
        least_coins[i] = best
    return least_coins[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
