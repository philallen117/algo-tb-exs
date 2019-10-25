# python3
import sys

def optimal_summands(n):
    assert n >= 1, "n not positive"
    summands = []
    balance = n
    prize = 1
    while True:
        # loop invariant prize <= balance
        if balance >= 2 * prize + 1:
            # safe to add prize and at least one further distinct value
            summands.append(prize)
            prize = prize + 1 # preserves loop invariant because guard
            continue
        elif balance < 2 * prize + 1:
            # cannot add more than one distinct summand
            # so add balance as final summand
            summands.append(balance)
            break
    return summands

if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
