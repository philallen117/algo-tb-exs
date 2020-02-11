# Uses python3

import re


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
        self.a[self.offset(i, j)] = v


def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False


def minMax(min1, max1, min2, max2, op):
    a, b = evalt(min1, min2, op), evalt(min1, max2, op)
    c, d = evalt(max1, min2, op), evalt(max1, max2, op)
    return min(a, b, c, d), max(a, b, c, d)


def options(i, j):
    # j >= i + 2
    return [((i, last1), (last1 + 1, j)) for last1 in range(i, j)]


def walkFrom2(n):
    # i'th element (0-based) of d'th diagonal
    return [(i, d + i) for d in range(2, n) for i in range(0, n - d)]


def maxv(nums, ops):
    n = len(nums)
    # n >= 3
    min_vals = UT0(n, 2305843009213693952)
    max_vals = UT0(n, -2305843009213693952)
    # Initialise 0th (main) diagonal
    for i, num in zip(range(n), nums):
        min_vals.set(i, i, num)
        max_vals.set(i, i, num)
    # 1st diagonal - one operation, no choice
    for i, j, vi, op, vj in zip(range(n-1), range(1, n), nums, ops, nums[1:]):
        v = evalt(vi, vj, op)
        min_vals.set(i, j, v)
        max_vals.set(i, j, v)
    for i, j in walkFrom2(n):
        for slice1, slice2 in options(i, j):
            min1 = min_vals.get(*slice1)
            max1 = max_vals.get(*slice1)
            min2 = min_vals.get(*slice2)
            max2 = max_vals.get(*slice2)
            min_opt, max_opt = minMax(min1, max1, min2, max2, ops[slice1[1]])
            min_old = min_vals.get(i, j)
            min_vals.set(i, j, min(min_old, min_opt))
            max_old = max_vals.get(i, j)
            max_vals.set(i, j, max(max_old, max_opt))
    return max_vals.get(0, n - 1)


def get_maximum_value(dataset):
    # parse input
    pnum = re.compile(r'\d+')
    pop = re.compile(r'\D')
    nums = list(map(int, pnum.findall(dataset)))
    ops = pop.findall(dataset)
    # simple cases
    n = len(nums)
    if n == 1:
        return nums[0]
    elif n == 2:
        return evalt(nums[0], nums[1], ops[0])
    else:
        return maxv(nums, ops)


if __name__ == "__main__":
    print(get_maximum_value(input()))
