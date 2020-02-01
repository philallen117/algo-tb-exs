#Uses python3

import sys

class TwoDArray:
    # 0-indexed
    def __init__(self, rows, cols):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.content = [0] * (rows * cols)

    def get(self, i, j):
        return self.content[i * self.cols + j]

    def set(self, i, j, value):
        self.content[i * self.cols + j] = value

def lcs2(s, t):
    rows, cols = len(s) + 1, len(t) + 1
    lcs = TwoDArray(rows, cols)
    # distance table - with s on rows and t on columns
    for row in range(1, rows):
        ss = s[row - 1]   # 0-indexed
        for col in range(1, cols):
            tt = t[col - 1]
            u = lcs.get(row - 1, col - 1)
            if ss == tt: u = u + 1
            v = lcs.get(row - 1, col)
            w = lcs.get(row, col - 1)
            lcs.set(row, col, max(u, v, w))
    return lcs.get(rows - 1, cols - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
