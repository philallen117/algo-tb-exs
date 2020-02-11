# Uses python3
import sys


class Array2:
    # 0-indexed
    def __init__(self, rows, cols, init_value=None):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.content = [init_value] * (rows * cols)

    def get(self, i, j):
        return self.content[i * self.cols + j]

    def set(self, i, j, value):
        self.content[i * self.cols + j] = value


def knapsack(W, ws, vs):
    n = len(ws)
    table = Array2(n + 1, W + 1)
    # table[i, u] will be best value of for knapsack capacity u
    # using first i weights (starting 0)
    for u in range(W + 1):  # Row 0 must be all 0
        table.set(0, u, 0)
    for i in range(1, n + 1):
        for u in range(W + 1):
            v_without_ith = table.get(i - 1, u)
            if ws[i - 1] > u:  # ith weight will not fit
                table.set(i, u, v_without_ith)
            else:  # i'th weight fits
                v_with_ith = table.get(i - 1, u - ws[i - 1]) + vs[i - 1]
                table.set(i, u, max(v_with_ith, v_without_ith))
    return table.get(n, W)


def optimal_weight(W, ws):
    # W limit, ws weights
    return knapsack(W, ws, vs)


if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
