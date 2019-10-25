# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    assert(capacity > 0)
    n = len(weights)
    rates = [values[i] / weights[i] for i in range(n)]
    table = zip(rates, weights, values)
    table = sorted(table, key = lambda row: row[0], reverse=True)
    for row in table:
        how_much = min(capacity, row[1])
        value = value + row[0] * how_much
        capacity = capacity - how_much
        if capacity == 0:
            break
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
