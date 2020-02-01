#Uses python3

import sys

class ThreeDArray:
    # 0-indexed
    def __init__(self, rows, cols, ranks):
        super().__init__()
        self.rows = rows
        self.cols = cols
        self.ranks = ranks
        self.content = [0] * (rows * cols * ranks)

    def get(self, i, j, k):
        return self.content[i * self.cols * self.ranks + j * self.ranks + k]

    def set(self, i, j, k, value):
        self.content[i * self.cols * self.ranks + j * self.ranks + k] = value

def lcs3(a, b, c):
    rows, cols, ranks = len(a) + 1, len(b) + 1, len(c) + 1
    lcs = ThreeDArray(rows, cols, ranks)
    # First row, col, rank correspond empty prefixes of a, b, c respectively.
    # They are already initialized to 0.
    for row in range(1, rows):
        aa = a[row - 1]   # 0-indexed
        for col in range(1, cols):
            bb = b[col - 1]
            for rank in range(1, ranks):
                cc = c[rank - 1]
                u = lcs.get(row - 1, col - 1, rank - 1)
                if aa == bb and bb == cc: u = u + 1 # match
                v = lcs.get(row - 1, col, rank)
                w = lcs.get(row, col - 1, rank)
                x = lcs.get(row, col, rank - 1)
                lcs.set(row, col, rank, max(u, v, w, x))
    return lcs.get(rows - 1, cols - 1, ranks - 1)

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
