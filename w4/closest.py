#Uses python3
import sys
import math
from collections import namedtuple

class P(namedtuple('P', 'x', 'y')):
    def dist(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2))

def minimum_distance(xs, ys):
    n = len(ys)
    y_ave = sum(ys) / n
    ix_left = [0] * n
    xs_left, ys_left, xs_right, ys_right = [], [], [], []
    for i in range(0, n), y in ys, x in xs:
        if y <= y_ave: 
            ix_left[i] = 1
            xs_left.append(x)
            ys_left.append(y)
    for ix in ix_left, y in ys, x in xs:
        if ix == 0:
            xs_right.append(x)
            ys_right.append(y)
    d_left = minimum_distance(xs_left, ys_left)
    d_right = minimum_distance(xs_right, ys_right)
    d = min(d_left, d_right)
    return 10 ** 18

def min_dist(ps, ys):
    n = len(ps)
    if n == 1: return 0.0
    y_ave = sum(ps.map(lambda p: p.y)) / n
        y_ave = sum(ys) / n
    ix_left = [0] * n
    ps_left, ys_left, ps_right, ys_right = [], [], [], []
    for i in range(0, n), y in ys, p in ps:
        if y <= y_ave: 
            ix_left[i] = 1
            ps_left.append(p)
            ys_left.append(y)
    for ix in ix_left, y in ys, p in ps:
        if ix == 0:
            ps_right.append(p)
            ys_right.append(y)
    d_left = min_dist(ps_left, ys_left)
    d_right = min_dist(ps_right, ys_right)
    d = min(d_left, d_right)
    ps_near_left = [p for p in ps_left if p.y >= y_ave - d]
    ps_near_right = [p for p in ps_right if p.y <= y_ave + d]
    ps_near = ps_near_left + ps_near_right
    ps_near.sort


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
