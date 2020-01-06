# Uses python3whi

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

def edit_distance(s, t):
    m, n = len(s), len(t)
    distances = TwoDArray(m + 1, n + 1)
    # distance table - with s on rows and t on columns
    for row in range(m + 1):
        distances.set(row, 0, row)
    for col in range(n + 1):
        distances.set(0, col, col)
    for row in range(1, m + 1):
        ss = s[row - 1]   # string 0-indexed
        for col in range(1, n + 1):
            # col j of 
            tt = t[col - 1]
            u = distances.get(row - 1, col - 1)
            if ss != tt: u = u + 1
            v = distances.get(row - 1, col) + 1
            w = distances.get(row, col - 1) + 1
            distances.set(row, col, min(u, v, w))
    return distances.get(m - 1, n - 1)

if __name__ == "__main__":
    print(edit_distance(input(), input()))
