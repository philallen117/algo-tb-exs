# Upper triangular square matrix with indices from 1 to n, initial value v


def sumto(k): return k * (k + 1) // 2


class UT0:
    def __init__(self, nn, v):
        self.n = nn
        self.m = sumto(nn)
        self.a = [v] * self.m

    def offset(self, i, j):
        ii = self.n - i - 1
        jj = self.n - j - 1
        return sumto(ii) + jj

    def get(self, i, j):
        return self.a[self.offset(i, j)]

    def set(self, i, j, v):
        self.a[self.__offset(i, j)] = v


class UT1:
    def __init__(self, nn, v):
        self.n = nn
        self.m = sumto(nn)
        self.a = [v] * self.m

    def offset(self, i, j):
        ii = self.n - i
        jj = self.n - j
        return sumto(ii) + jj

    def get(self, i, j):
        return self.a[self.offset(i, j)]

    def set(self, i, j, v):
        self.a[self.__offset(i, j)] = v
